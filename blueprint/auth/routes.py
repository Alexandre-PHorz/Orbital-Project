from . import auth
from flask import render_template, request, url_for, redirect
from data import verify_user
from flask_login import UserMixin



@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/log',methods=['POST'])
def log():
    cpf = request.form.get('cpf')
    password = request.form.get('password')
    if verify_user(cpf, password):
        return redirect(url_for('client.home_aluno'))
    else:
        return "Erro ao logar usuário", 404