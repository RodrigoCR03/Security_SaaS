from app import db

class AVSDSession(db.Model):
    __tablename__ = 'avsd_sessions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    session_data = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Outros campos relevantes
