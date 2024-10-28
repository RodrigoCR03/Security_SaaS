from flask import Blueprint, jsonify, request
from app.models.user import User
from app.utils.security import token_required
from app import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile', methods=['GET'])
@token_required
def get_profile(current_user):
    user_data = {
        'id': current_user.id,
        'email': current_user.email,
        'name': current_user.name,
        'role': current_user.role
    }
    return jsonify({'user': user_data}), 200

@user_bp.route('/update', methods=['PUT'])
@token_required
def update_profile(current_user):
    data = request.get_json()
    current_user.name = data.get('name', current_user.name)
    db.session.commit()
    return jsonify({'message': 'Perfil atualizado com sucesso'}), 200

@user_bp.route('/change_password', methods=['PUT'])
@token_required
def change_password(current_user):
    data = request.get_json()
    old_password = data.get('old_password')
    new_password = data.get('new_password')

    if not current_user.check_password(old_password):
        return jsonify({'message': 'Senha antiga incorreta'}), 400

    current_user.set_password(new_password)
    db.session.commit()
    return jsonify({'message': 'Senha atualizada com sucesso'}), 200
