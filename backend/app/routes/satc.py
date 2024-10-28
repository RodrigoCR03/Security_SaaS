from flask import Blueprint, jsonify
from app.utils.security import token_required
from app.services.satc_service import start_simulation, get_simulation_results

satc_bp = Blueprint('satc', __name__)

@satc_bp.route('/start', methods=['POST'])
@token_required
def start_satc(current_user):
    simulation_id = start_simulation(current_user.id)
    return jsonify({'message': 'Simulação iniciada', 'simulation_id': simulation_id}), 200

@satc_bp.route('/results/<int:simulation_id>', methods=['GET'])
@token_required
def simulation_results(current_user, simulation_id):
    results = get_simulation_results(current_user.id, simulation_id)
    if not results:
        return jsonify({'message': 'Resultados não encontrados'}), 404
    return jsonify({'results': results}), 200
