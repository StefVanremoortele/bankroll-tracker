from flask import Blueprint

bp = Blueprint('sessions', __name__, url_prefix='/sessions')

@bp.route('/', methods=['GET'])
def list_sessions():
    return {'sessions': []}  # placeholder

@bp.route('/', methods=['POST'])
def create_session():
    return {'message': 'create session (not implemented yet)'}

@bp.route('/<int:session_id>', methods=['PATCH'])
def update_session(session_id):
    return {'message': f'update session {session_id} (not implemented yet)'}
