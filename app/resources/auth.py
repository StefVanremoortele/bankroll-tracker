from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['POST'])
def login():
    return {'token': 'fake-token'}  # Replace with real JWT implementation later
