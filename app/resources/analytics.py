from flask import Blueprint

bp = Blueprint('analytics', __name__, url_prefix='/analytics')

@bp.route('/summary', methods=['GET'])
def summary():
    # placeholder summary
    return {
        'total_profit': 0.0,
        'sessions_count': 0,
        'average_hourly': 0.0
    }
