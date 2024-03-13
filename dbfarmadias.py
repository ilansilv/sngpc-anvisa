from flask import Flask
import psycopg2
import requests


app = Flask(__name__)

def conectar_banco():
    try:
        conn = psycopg2.connect(
            dbname='farmadias',
            user='postgres',
            password='postgres',
            host='localhost'
        )

        return conn
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None

@app.route('/entidade')
def index():
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()

        cursor.execute ("select * from entidade;")
        resultados = cursor.fetchall()

        for resultado in resultados:
            print(resultado)

        cursor.close()
        conexao.close()

        return 'Operação realizada com sucesso'
    else:
        return 'Erro ao conectar ao banco de dados'




app.run()