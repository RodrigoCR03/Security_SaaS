from app import db

class PrivacySettings(db.Model):
    __tablename__ = 'privacy_settings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tracking_cookies = db.Column(db.Boolean, default=True)
    history_cleanup = db.Column(db.Boolean, default=True)
    data_monitoring = db.Column(db.Boolean, default=True)

    # Outros campos de configuração
