from flask import Flask, request, jsonify
from http import HTTPStatus
app = Flask(__name__)

usuarios = []

proximo_id = 1


@app.route('/users', methods=['POST'])

def criar_usuario():
    global proximo_id

    dados = request.json

    if not dados or 'nome' not in dados or 'email' not in dados:
        return jsonify({'erro': 'Campo nome e email são obrigatorios'}), HTTPStatus.BAD_REQUEST
    
    novo_usuario = {
        'id': proximo_id,
        'nome': dados['nome'],
        'email': dados['email']
    }

    usuarios.append(novo_usuario)
    proximo_id += 1

    return jsonify(novo_usuario), HTTPStatus.CREATED


if __name__ == '__main__':
    app.run(debug=True)