import numpy as np
from app.models.threat import Threat
from app import db

def analyze_user_behavior(user_id):
    user_activity = get_user_activity(user_id)
    anomalies = detect_anomalies(user_activity)
    for anomaly in anomalies:
        threat = Threat(
            user_id=user_id,
            threat_type='Anomalia Detectada',
            description='Atividade anômala detectada: {}'.format(anomaly),
            severity='Alta'
        )
        db.session.add(threat)
    db.session.commit()

def get_user_activity(user_id):
    # Implementar a lógica para obter dados reais de atividade do utilizador
    # Exemplo:
    data = np.random.normal(0, 1, 100)
    return data

def detect_anomalies(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    threshold = mean + 2 * std_dev
    anomalies = data[data > threshold]
    return anomalies
