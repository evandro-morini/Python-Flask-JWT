from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask import request, jsonify
from ..models.revendedor import Revendedor, revendedor_schema


def post_revendedor():
    nome = request.json['nome']
    email = request.json['email']
    cpf = request.json['cpf']
    senha = request.json['senha']
    hash = generate_password_hash(senha)
    revendedor = Revendedor(nome, email, cpf, hash)

    try:
        db.session.add(revendedor)
        db.session.commit()
        result = revendedor_schema.dump(revendedor)
        return jsonify({'message': 'Revendedor cadastrado com sucesso', 'data': result}), 200
    except:
        return jsonify({'message': 'Erro ao criar revendedor', 'data': {}}), 500


def validar_login():
    email = request.json['email']
    revendedor = Revendedor.query.filter(Revendedor.email == email).one()
    if not revendedor:
        return jsonify({'message': "Revendedor não encontrado", 'data': {}}), 404

    senha = request.json['senha']

    if check_password_hash(revendedor.senha, senha):
        return jsonify({'message': 'Autorizado', 'id': revendedor.id}), 200
    else:
        return jsonify({'message': "Não Autorizado", 'data': {}}), 401


def revendedor_by_email(email):
    try:
        return Revendedor.query.filter(Revendedor.email == email).one()
    except:
        return None