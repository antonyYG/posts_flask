from flask import Flask, render_template, session, redirect, url_for
from config import Config
from app.extensions import db, bcrypt
from app.controllers import user_controller, post_controller

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    bcrypt.init_app(app)

    # Registrar rutas
    user_controller.register_routes(app)
    post_controller.register_routes(app)

    @app.route('/')
    def index():
        if 'user_id' in session:
            return redirect(url_for('list_posts'))
        return render_template('login.html')

    return app

app = create_app()
