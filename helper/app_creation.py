from flask import Flask
from project.config.development import Development
def create_app(db):
    app = Flask(__name__)
    app.config.from_object(Development)
    db.init_app(app)
    with app.app_context():
        from project.feature.auth.route import auth_bp
        from project.feature.user.route import user_bp
        from project.feature.match.route import match_bp
        from project.feature.team.route import team_bp
        app.register_blueprint(auth_bp)
        app.register_blueprint(user_bp)
        app.register_blueprint(match_bp)
        app.register_blueprint(team_bp)
        # print(app.url_map)
        return app