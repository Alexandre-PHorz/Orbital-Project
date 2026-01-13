from flask import Flask
from flask import render_template, session, url_for, redirect
from functools import wraps
from dotenv import load_dotenv
from blueprint.auth import auth
from blueprint.client import client
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.register_blueprint(auth)
app.register_blueprint(client)

def get_user_session(function):
    @wraps(function) # Essencial para o Flask não se confundir
    def wrapper(*args, **kwargs): # Aceita argumentos da rota (como IDs)
        if 'user' in session:
            return function(*args, **kwargs)
        else:
            # Redireciona de fato o usuário para a página de login
            return redirect(url_for('auth.login'))
    return wrapper


@app.route('/')
@get_user_session
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(port=8080, debug=True)