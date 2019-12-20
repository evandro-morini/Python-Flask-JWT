from app import app
from flask import request, jsonify
import jwt
import datetime
from werkzeug.security import check_password_hash
from functools import wraps
from .revendedor import revendedor_by_email


def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Erro de autenticação', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

    revendedor = revendedor_by_email(auth.username)
    if not revendedor:
        return jsonify({'message': 'Revendedor não encontrado', 'data': {}}), 401

    if revendedor and check_password_hash(revendedor.senha, auth.password):
        token = jwt.encode({'username': revendedor.email, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)}, app.config['SECRET_KEY'])
        return jsonify({'message': 'Validado com sucesso!', 'token': token.decode('UTF-8'), 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})

    return jsonify({'message': 'Erro de autenticação', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token não encontrado', 'data': {}}), 401

        try:
            jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Token inválido ou expirado', 'data': {}}), 401
        return f(*args, **kwargs)
    return decorated