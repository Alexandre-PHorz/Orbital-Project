from . import client
from data import show_inst
from flask import render_template


@client.route('/')
def home_aluno():
    return render_template('home_aluno.html',insts = show_inst())