from app import app
from flask import jsonify
from ..views import revendedor, compra, helper


@app.route('/', methods=['GET'])
def root():
    return jsonify({'message' : 'Teste Boticário API Revendedores por Evandro Morini'})


@app.route('/auth', methods=['POST'])
def authenticate():
    return helper.auth()


@app.route('/revendedor/add', methods=['POST'])
@helper.token_required
def post_revendedor():
    return revendedor.post_revendedor()


@app.route('/revendedor/validar_login', methods=['POST'])
@helper.token_required
def validar_login():
    return revendedor.validar_login()


@app.route('/compra/add', methods=['POST'])
@helper.token_required
def post_compra():
    return compra.post_compra()


@app.route('/compra/update/<id>', methods=['PUT'])
@helper.token_required
def update_compra(id):
    return compra.update_compra(id)


@app.route('/compra/delete/<id>', methods=['DELETE'])
@helper.token_required
def delete_compra(id):
    return compra.delete_compra(id)


@app.route('/compra/list', methods=['GET'])
@helper.token_required
def get_compras():
    return compra.get_compras()


@app.route('/compra/acumulado', methods=['GET'])
@helper.token_required
def get_acumulado():
    return compra.get_acumulado()