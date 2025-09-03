from flask import Blueprint, jsonify
from app.models.bankroll import Bankroll

bp = Blueprint('bankrolls', __name__, url_prefix='/bankrolls')

@bp.route('/', methods=['GET'])
def get_bankrolls():
    
    bankrolls = Bankroll.query.all()
    return jsonify([b.to_dict() for b in bankrolls])

@bp.route('/', methods=['POST'])
def create_bankroll():
    return {'message': 'create bankroll (not implemented yet)'}

@bp.route('/<int:bankroll_id>', methods=['PUT'])
def update_bankroll(bankroll_id):
    return {'message': f'update bankroll {bankroll_id} (not implemented yet)'}
