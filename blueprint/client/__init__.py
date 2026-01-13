from flask import Blueprint

client = Blueprint(
    'client',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/aluno'
)

from . import routes