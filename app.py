from flask import Flask, jsonify, request

app = Flask(__name__)


#onde os dados estão armazenados
clientes = [
    {
        'id': 1,
        'nome': 'Ilan',
        'cidade': 'Camaragibe',
        'idade': 30
    },
    {
        'id': 2,
        'nome': 'Sintique',
        'cidade': 'Recife',
        'idade': 29
    },
    {
        'id': 3,
        'nome': 'Lea',
        'cidade': 'Camaragibe',
        'idade': 65
    },
    {
        'id': 4,
        'nome': 'Joao',
        'cidade': 'Palmares',
        'idade': 30
    },
]

#consultar todos
@app.route('/consultar',methods=['GET'])
def consultar_clientes():
    return jsonify(clientes)

#consulta individual pelo id
@app.route('/consultar/<int:id>',methods=['GET'])
def consulta_individual(id):
    for cliente in clientes:
        if cliente.get('id') == id:
            return jsonify(cliente)
        
#editar por id
@app.route('/consultar/<int:id>', methods=['PUT'])
def editar_clientes_id(id):
    cliente_alterado = request.get_json()
    for indice,cliente in enumerate(clientes):
        if cliente.get('id') == id:
            clientes[indice].update(cliente_alterado)
            return jsonify(clientes[indice])
        
#criar ou incluir
@app.route('/consultar',methods=['POST'])
def incluir_cliente():
    novo_cliente = request.get_json()
    clientes.append(novo_cliente)

    return jsonify(clientes)

#excluir
@app.route('/consultar/<int:id>',methods=['DELETE'])
def excluir_cliente(id):
    for indice, cliente in enumerate(clientes):
        if cliente.get('id') == id:
            del clientes[indice]

    return jsonify(clientes)


app.run(port=5000,host='localhost',debug=True)