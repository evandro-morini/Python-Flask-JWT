import requests
from app import db
from flask import request, jsonify, current_app
from ..models.revendedor import Revendedor
from ..models.compra import Compra, compra_schema, compras_schema


def post_compra():
    valor = float(request.json['valor'])
    cpf = request.json['cpf']
    revendedor = Revendedor.query.filter(Revendedor.cpf == cpf).one()
    if not revendedor:
        return jsonify({'message': "Revendedor não encontrado", 'data': {}}), 404

    if valor < 1000.00:
        cashback = valor * 0.10
    elif valor >= 1000.00 and valor < 1500.00:
        cashback = valor * 0.15
    elif valor > 1500.00:
        cashback = valor * 0.20

    if revendedor.cpf == '15350946056':
        status = 2 #Aprovado
    else:
        status = 1 #Em validação

    compra = Compra(valor, revendedor.id, cashback, status)

    try:
        db.session.add(compra)
        db.session.commit()
        result = compra_schema.dump(compra)
        return jsonify({'message': 'Compra cadastrada com sucesso', 'data': result}), 200
    except:
        return jsonify({'message': 'Erro ao criar compra', 'data': {}}), 500


def update_compra(id):
    compra = Compra.query.get(id)
    if not compra:
        return jsonify({'message': "Compra não encontrada", 'data': {}}), 404
    if compra.status == 2:
        return jsonify({'message': "Não é possível alterar: Compra já Aprovada!", 'data': {}}), 500

    valor = float(request.json['valor'])
    status = int(request.json['status'])
    cpf = request.json['cpf']
    revendedor = Revendedor.query.filter(Revendedor.cpf == cpf).one()
    if not revendedor:
        return jsonify({'message': "Revendedor não encontrado", 'data': {}}), 404

    if valor < 1000.00:
        cashback = valor * 0.10
    elif valor >= 1000.00 and valor < 1500.00:
        cashback = valor * 0.15
    elif valor > 1500.00:
        cashback = valor * 0.20

    if compra:
        try:
            compra.valor = valor
            compra.status = status
            compra.revendedor_id = revendedor.id
            compra.cashback = cashback
            db.session.commit()
            result = compra_schema.dump(compra)
            return jsonify({'message': 'Compra alterada com sucesso', 'data': result}), 200
        except:
            return jsonify({'message': 'Erro ao alterar compra', 'data': {}}), 500


def delete_compra(id):
    compra = Compra.query.get(id)
    if not compra:
        return jsonify({'message': "Compra não encontrada", 'data': {}}), 404
    if compra.status == 2:
        return jsonify({'message': "Não é possível excluir: Compra já Aprovada!", 'data': {}}), 500
    else:
        try:
            db.session.delete(compra)
            db.session.commit()
            result = compra_schema.dump(compra)
            return jsonify({'message': 'Compra excluída com sucesso', 'data': result}), 200
        except:
            return jsonify({'message': 'Erro ao excluir compra', 'data': {}}), 500


def get_compras():
    compras = Compra.query.all()
    if compras:
        result = compras_schema.dump(compras)
        return jsonify({'message': 'Compras carregadas!', 'data': result})

    return jsonify({'message': 'Nenhuma compra foi encontrada!', 'data': {}})


def get_acumulado():
    cpf = request.args.get('cpf')
    if cpf:
        params = dict(cpf=cpf)
        url = current_app.config['BOTICARIO_ACUMULADO_URI']
        response = requests.get(url=url, params=params)

    return response.json()