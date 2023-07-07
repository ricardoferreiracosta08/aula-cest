from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Recurso fictício - Lista de usuários
users = [
    {"id": 1, "name": "João"},
    {"id": 2, "name": "Maria"},
    {"id": 3, "name": "Pedro"}
]

# Rota da página inicial
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', users=users)

# Endpoint para listar todos os usuários
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Endpoint para criar um novo usuário
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(new_user), 201

# Endpoint para obter um usuário específico
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return jsonify(user)
    return jsonify({"error": "Usuário não encontrado"}), 404

# Endpoint para atualizar um usuário existente
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    updated_user = request.get_json()
    for user in users:
        if user['id'] == user_id:
            user['name'] = updated_user['name']
            return jsonify(user)
    return jsonify({"error": "Usuário não encontrado"}), 404

# Endpoint para deletar um usuário existente
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            return jsonify({"message": "Usuário removido com sucesso"})
    return jsonify({"error": "Usuário não encontrado"}), 404

if __name__ == '__main__':
    app.run()
