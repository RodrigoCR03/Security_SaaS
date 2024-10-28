from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(100))
    role = db.Column(db.String(50), default='user')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    threats = db.relationship('Threat', backref='user', lazy=True)
    privacy_settings = db.relationship('PrivacySettings', backref='user', uselist=False)
    avsd_sessions = db.relationship('AVSDSession', backref='user', lazy=True)
    # Outros relacionamentos

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
