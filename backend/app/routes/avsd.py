from flask import Blueprint, jsonify, request
from app.utils.security import token_required
from app.services.ai.avsd_service import get_avsd_response

avsd_bp = Blueprint('avsd', __name__)

@avsd_bp.route('/chat', methods=['POST'])
@token_required
def avsd_chat(current_user):
    data = request.get_json()
    user_input = data.get('message')
    if not user_input:
        return jsonify({'message': 'Nenhuma mensagem fornecida'}), 400

    response = get_avsd_response(user_input)
    return jsonify({'response': response}), 200
