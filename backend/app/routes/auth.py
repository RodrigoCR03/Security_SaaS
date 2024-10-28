from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db
from app.utils.security import generate_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')

    if not email or not password:
        return jsonify({'message': 'Email e senha são obrigatórios.'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email já registrado.'}), 400

    new_user = User(email=email, name=name)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    token = generate_token(new_user)

    return jsonify({'message': 'Usuário registrado com sucesso', 'token': token}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email e senha são obrigatórios.'}), 400

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        token = generate_token(user)
        return jsonify({'message': 'Login realizado com sucesso', 'token': token}), 200
    else:
        return jsonify({'message': 'Credenciais inválidas'}), 401
