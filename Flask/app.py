from flask import Flask, jsonify, request

app = Flask(__name__)

banco_de_dados = []

def gerador_de_id():
    return len(banco_de_dados)+1

@app.route('/users', methods=['GET']) #retorna todos usuarios
def get_users():
    dados = banco_de_dados
    return jsonify(dados), 200

@app.route('/users/<int:user_id>', methods=['GET']) #retorna um usuario especifico
def get_user(user_id):
    for usuario in banco_de_dados:
        if usuario['id'] == user_id:
            return jsonify({'msg:': f'Usuário {usuario["nome"]} encontrado'}), 202
        
    return jsonify({'erro': 'usuário não encontrado'}), 404




@app.route('/users/create', methods=['GET', 'POST'])    #Cria um usuario 
def create_users():

    current_id = gerador_de_id()
    nome = request.args.get('nome')
    email = request.args.get('email')

    usuario_new = {'id' : current_id, 'nome': nome, 'email': email}
    banco_de_dados.append(usuario_new)

    return jsonify({'msg' : f'Usuário {usuario_new["nome"]} cadastrado com sucesso'}), 201

@app.route('/users/<int:user_id>', methods=['PUT']) #Edita um usuario

def update_user(user_id):
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')

    for usuario in banco_de_dados:
        if usuario['id'] == user_id:
            if nome:
                usuario['nome'] = nome
            if email:
                usuario['email'] = email

            return jsonify(usuario), 200

    return jsonify({'erro': 'usuário não encontrado'}), 404
           
    



@app.route('/users/delete/<int:user_id>', methods=['DELETE']) #Deleta um usuario
def delete_user(user_id):

    for usuario in banco_de_dados:
        if usuario['id'] == user_id:
            banco_de_dados.remove(usuario)
            return jsonify({'msg:':f'Usuário {usuario["nome"]} deletado com sucesso'}), 200

    
    return jsonify({'erro': 'usuário não encontrado'}), 404
    
    


if __name__ == '__main__':
    app.run(debug=True)