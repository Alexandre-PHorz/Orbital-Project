from . import auth
from flask import render_template, request
from data import verify_user



@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/log',methods=['POST'])
def log():
    cpf = request.form.get('cpf')
    password = request.form.get('password')
    if verify_user(cpf, password):
        return "Usuário logado com sucesso"
    else:
        return "Erro ao logar usuário", 404