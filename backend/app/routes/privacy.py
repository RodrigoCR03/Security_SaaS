from flask import Blueprint, jsonify, request
from app.utils.security import token_required
from app.models.privacy import PrivacySettings
from app import db

privacy_bp = Blueprint('privacy', __name__)

@privacy_bp.route('/settings', methods=['GET'])
@token_required
def get_privacy_settings(current_user):
    settings = PrivacySettings.query.filter_by(user_id=current_user.id).first()
    if not settings:
        settings = PrivacySettings(user_id=current_user.id)
        db.session.add(settings)
        db.session.commit()

    settings_data = {
        'tracking_cookies': settings.tracking_cookies,
        'history_cleanup': settings.history_cleanup,
        'data_monitoring': settings.data_monitoring
    }
    return jsonify({'settings': settings_data}), 200

@privacy_bp.route('/settings', methods=['PUT'])
@token_required
def update_privacy_settings(current_user):
    data = request.get_json()
    settings = PrivacySettings.query.filter_by(user_id=current_user.id).first()
    if not settings:
        settings = PrivacySettings(user_id=current_user.id)

    settings.tracking_cookies = data.get('tracking_cookies', settings.tracking_cookies)
    settings.history_cleanup = data.get('history_cleanup', settings.history_cleanup)
    settings.data_monitoring = data.get('data_monitoring', settings.data_monitoring)

    db.session.add(settings)
    db.session.commit()

    return jsonify({'message': 'Configurações de privacidade atualizadas com sucesso'}), 200
