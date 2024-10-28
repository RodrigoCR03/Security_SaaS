from flask import Blueprint, jsonify
from app.utils.security import token_required
from app.services.ai.anomaly_detection import get_user_threats

threat_bp = Blueprint('threat', __name__)

@threat_bp.route('/list', methods=['GET'])
@token_required
def list_threats(current_user):
    threats = get_user_threats(current_user.id)
    return jsonify({'threats': threats}), 200

@threat_bp.route('/details/<int:threat_id>', methods=['GET'])
@token_required
def threat_details(current_user, threat_id):
    threat = Threat.query.filter_by(id=threat_id, user_id=current_user.id).first()
    if not threat:
        return jsonify({'message': 'Ameaça não encontrada'}), 404

    threat_data = {
        'id': threat.id,
        'type': threat.threat_type,
        'description': threat.description,
        'severity': threat.severity,
        'timestamp': threat.timestamp
    }
    return jsonify({'threat': threat_data}), 200
