from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# config import
from config import app_config, app_active

config = app_config[app_active]


def create_app(config_name):
    app = Flask(__name__, template_folder='templates')
    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(config.APP)
    db.init_app(app)

    @app.route('/')
    def index():
        return 'Meu primeiro run'

    @app.route('/login/')
    def login():
        return 'Aqui entrará a tela de login'

    @app.route('/recovery-password/')
    def recovery_password():
        return 'Aqui entrará a tela de recuperar senha'

    @app.route('/profile/<int:user_id>/action/<action>/')
    def profile(user_id, action):
        if action == 'action1':
            return f'Ação1 {action} usuário de ID {user_id}'
        elif action == 'action2':
            return f'Ação2 {action} usuário de ID {user_id}'
        else:
            return f'Ação default for userId {user_id}'

    @app.route('/profile/', methods=['POST'])
    def create_profile():
        username = request.form['username']
        password = request.form['password']
        return f'Essa rota possui um método POST e criará um usuário com os dados de usuário {username} e senha ' \
               f'{password}'

    @app.route('/profile/<int:id>', methods=['PUT'])
    def edit_total_profile(id):
        username = request.form['username']
        password = request.form['password']
        return f'PUT username: {username}, password: {password}'

    return app
