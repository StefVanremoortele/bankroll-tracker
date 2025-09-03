from flask import Blueprint
# from app.models import bankroll
from flask import jsonify
from app.models.bankroll import Bankroll
from app.models.user import User
from app.extensions import db

bp = Blueprint('users', __name__, url_prefix='/users')



@bp.route('/', methods=['GET'])
def get_users():
    # from app.models import bankroll, user
    

    users = User.query.all()
    users_list = [u.to_dict() for u in users]

    # return {'users': users_list}  # Replace with real JWT implementation later
    return jsonify(users_list)


### SQL ALCHEMY SESSIONS EXAMPLE ###
# new_bankroll = Bankroll(user_id=1, name='Main Live', currency='EUR', starting_balance=1000)
# db.session.add(new_bankroll)

# new_user = User(email="stef@gmail.com")
# new_user.set_password("test")
# db.session.add(new_user)

# db.session.commit()