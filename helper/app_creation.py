from flask import Flask
from project.config.development import Development
def create_app(db):
    app = Flask(__name__)
    app.config.from_object(Development)
    db.init_app(app)
    with app.app_context():
        from project.feature.auth.route import auth_bp
        app.register_blueprint(auth_bp)
        return app