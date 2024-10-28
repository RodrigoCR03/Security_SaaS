import datetime
import jwt
from flask import request, jsonify
from functools import wraps
from app.models.user import User
from app.config import Config

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token não encontrado!'}), 401
        try:
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            current_user = User.query.filter_by(id=data['id']).first()
            if current_user is None:
                raise Exception('Usuário não encontrado')
        except Exception as e:
            return jsonify({'message': 'Token inválido!', 'error': str(e)}), 401
        return f(current_user, *args, **kwargs)
    return decorated

def generate_token(user):
    token = jwt.encode({
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=12)
    }, Config.SECRET_KEY, algorithm="HS256")
    return token
