import os
import bcrypt
from uuid import uuid4
from dotenv import load_dotenv
from validate_docbr import CPF
from mysql.connector import connect, Error

load_dotenv()

# Função para garantir que sempre teremos uma conexão válida
def get_db_connection():
    return connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

def verify_user(cpf, password):
    cpf_validator = CPF()
    if not cpf_validator.validate(cpf):
        return False

    try:
        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                query = "SELECT senha from tb_usuarios WHERE cpf = %s"
                cursor.execute(query, (cpf,))
                result = cursor.fetchone()
                if result:
                    stored_hashed_password = result[0].encode('utf-8')
                    return bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password)
                else:
                    return False
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return False

def add_user(name, cpf:str, password:str, inst,tipo:str = 'alu'):
    cpf_validator = CPF()
    cpf = cpf.strip().replace('.','').replace('-','')
    if not cpf_validator.validate(cpf):
        return False, 'CPF Invalido!'

    try:
        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                query = 'SELECT id FROM tb_usuarios WHERE=%s'
                cursor.execute(query,(cpf,))
                if cursor.fetchone():
                    return False, 'Já contem uma conta nesse CPF'
                sign = 'INSERT INTO tb_usuarios VALUE(%s,%s,%s,%s,%s,%s)'
                cursor.execute(query,(str(uuid4().hex)[:9],name,bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=12)),cpf,inst,tipo))
                cursor.commit()

                return True
                
    except:
        return False