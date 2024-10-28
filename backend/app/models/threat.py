from app import db

class Threat(db.Model):
    __tablename__ = 'threats'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    threat_type = db.Column(db.String(100))
    description = db.Column(db.Text)
    severity = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Outros campos relevantes
