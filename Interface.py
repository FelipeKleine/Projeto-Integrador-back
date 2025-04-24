from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

#Cria o servidor
app = Flask(__name__)
#Cria o BD utilizando a biblioteca flask_sqlalchemy que salva os dados em usuario.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'  # Arquivo do banco de dados SQLite
#variavel para utilizar o BD no script
db = SQLAlchemy(app)



# Definição do modelo do usuário no banco de dados. As caracteristicas principias do usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    data_cadastro = db.Column(db.DateTime, default=datetime.now)
#Perfil do usuario que estou aprimorando, será uma nova coluna no BD 
#    formulario = db.Column(db.Integer)

#Função de segurança para omitir a senha gerando uma hash
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

#Função para checar senha
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Usuario {self.username}>'

with app.app_context():
    db.create_all()  # Cria as tabelas no banco de dados


#Direciona para pagina principal
@app.route ('/', methods=["GET", "POST"])
def Inicio():
    return render_template('index2.html')


#Função para conferir as credenciais do usuario ao acessar seu Login
@app.route('/Login', methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'erro': 'Nome de usuário e senha são obrigatórios.'}), 400

        usuario = Usuario.query.filter_by(username=username).first()

        if usuario and usuario.check_password(password):
            # Autenticação bem-sucedida, retorna informações do perfil (você pode ajustar quais informações retornar)
            return jsonify({'id': usuario.id, 'username': usuario.username, 'email': usuario.email}), 200
        else:
            return jsonify({'erro': 'Credenciais inválidas.'}), 401


    return render_template("perfil.html")


#Função para criar um Login do usuario
@app.route('/Cadastro', methods=["POST", "GET"])
def Cadastro():
    if request.method == "POST":
        dados = request.get_json()
        if 'username' in dados and 'email' in dados and 'password' in dados:
            username = dados['username']
            email = dados['email']
            password = dados['password']


            if Usuario.query.filter_by(username=username).first():
                return jsonify({'erro': 'Nome de usuário já existe.'}), 409
            if Usuario.query.filter_by(email=email).first():
                return jsonify({'erro': 'Email já cadastrado.'}), 409

            novo_usuario = Usuario(username=username, email=email)
            novo_usuario.set_password(password)

            db.session.add(novo_usuario)
            db.session.commit()
            

            return jsonify({'mensagem': 'Usuário cadastrado com sucesso!', 'id': novo_usuario.id}), 201
        else:
            return jsonify({'erro': 'Dados de cadastro incompletos.'}), 400
    return render_template("cadastro.html")


#Função que retorna as informações do perfil do usuario 
@app.route('/Usuario_perfil/<int:id>', methods=["GET"])
def exibir_perfil(id):
    usuario = Usuario.query.get_or_404(id)
    return render_template("usuario.html", usuario=usuario)

#Essa função está em desenvolvimento
@app.route('/Usuario_perfil/Calcular', methods=["GET"])
def Calcular_perfil(id):

    return render_template("calculo.html", usuario=usuario)


if __name__ == '__main__':
    app.run(debug=True)





