from flask import Flask
from .extensions import db, ma, jwt
from .config import Config
from .models.bankroll import Bankroll
from .models.user import User
# from .models import 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from .resources import auth, bankrolls, sessions, analytics, users
        app.register_blueprint(auth.bp)
        app.register_blueprint(users.bp)
        app.register_blueprint(bankrolls.bp)
        app.register_blueprint(sessions.bp)
        app.register_blueprint(analytics.bp)

        db.create_all()  # For dev only; use Alembic in production

    @app.route('/health')
    def health():
        return {'status': 'ok'}

    return app
