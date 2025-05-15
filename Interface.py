from flask import Flask, request, jsonify, render_template, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'  # Arquivo do banco de dados SQLite
db = SQLAlchemy(app)


# Definição do modelo do usuário no banco de dados
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    data_cadastro = db.Column(db.DateTime, default=datetime.now)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Usuario {self.username}>'
    



with app.app_context():
    db.create_all()  # Cria as tabelas no banco de dados, se não existirem


#Página inicial
@app.route ('/', methods=["GET", "POST"])
def Inicio():
    return render_template('index2.html')

#Página orcamento
@app.route ('/orcamento', methods=["GET", "POST"])
def orcamento():
    return render_template('orcamento.html')

#Página GerencieDividas
@app.route ('/gerenciedividas', methods=["GET", "POST"])
def gerenciedividas():
    return render_template('gerenciedividas.html')

#Página criemetas
@app.route ('/criemetas', methods=["GET", "POST"])
def criemetas():
    return render_template('criemetas.html')

#Página conceitosfundamentais
@app.route ('/conceitosfundamentais', methods=["GET", "POST"])
def conceitosfundamentais ():
    return render_template('conceitosfundamentais.html')

#Página tiposinvestimentos
@app.route ('/tiposinvestimentos', methods=["GET", "POST"])
def tiposinvestimentos ():
    return render_template('tiposinvestimentos.html')


#Página risco
@app.route ('/risco', methods=["GET", "POST"])
def risco ():
    return render_template('risco.html')



#Página cursos
@app.route ('/cursos', methods=["GET", "POST"])
def cursos ():
    return render_template('cursos.html')

#Página leituras
@app.route ('/leituras', methods=["GET", "POST"])
def leituras ():
    return render_template('leituras.html')

#Páginna noticias
@app.route ('/noticias', methods=["GET", "POST"])
def noticias ():
    return render_template('noticias.html')

@app.route('/')
def home():
    return render_template('index2.html')

#Função de Login
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


#Função de cadastro
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


#Função de exibição do perfil já cadastrado, definido por ID
@app.route('/Usuario_perfil/<int:id>', methods=["GET"])
def exibir_perfil(id):
    usuario = Usuario.query.get_or_404(id)
    return render_template("usuario.html", usuario=usuario)

#Em desenvolvimento!
RespostasFormulario = []
@app.route('/Calcular', methods=["GET", "POST"])
def Calcular_perfil():
    if request.method == "POST":
        respostas = request.get_json()
        if 'r1' in respostas and 'r2' in respostas and 'r3' in respostas and 'r4' in respostas:
            R1 = respostas['r1']
            RespostasFormulario.append[R1]
            R2 = respostas['r2']
            RespostasFormulario.append[R2]
            R3 = respostas['r3']
            RespostasFormulario.append[R3]
            R4 = respostas['r4']
            RespostasFormulario.append[R4]
            return jsonify({'mensagem': 'Formulario preenchido!'}), 201
        else:
            return jsonify({'erro': 'Falha!'})

    return render_template("calculo.html")


# Função de exibição do formulario de identificação do perfil
@app.route('/Perfil_investidor', methods=["GET"])
def exibir_resultado():
    Respostas = RespostasFormulario
    return render_template('perfil_inv.html', Respostas=Respostas)

#Função para executar o botão de Tipos de Investimentos
@app.route('/Tipos_investimento', methods=["POST", "GET"])
def tipos_investimento():
    return render_template('tipos.html')

#Função de rota da calculadora
@app.route('/Calculadora', methods=["POST", "GET"])
def calculadora():
    return render_template('calculadora.html')


#Função para executar os calculos com os parametros estabelecidos
def calcular_investimento(valor_inicial, aporte_mensal, taxa_anual, periodo, tipo_periodo, tipo_investimento, tributacao):
    taxa_mensal = (1 + taxa_anual / 100) ** (1/12) - 1
    if tipo_periodo == 'years':
        num_meses = periodo * 12
    else:
        num_meses = periodo

    montante_final = valor_inicial * (1 + taxa_mensal) ** num_meses
    for _ in range(num_meses):
        montante_final += aporte_mensal * (1 + taxa_mensal) ** (num_meses - _)

    total_investido = valor_inicial + (aporte_mensal * num_meses)
    juros_bruto = montante_final - total_investido
    imposto = juros_bruto * (tributacao / 100)
    montante_liquido = montante_final - imposto

    return {
        'total_investido': round(total_investido, 2),
        'juros_acumulados': round(juros_bruto, 2),
        'imposto_deduzido': round(imposto, 2),
        'valor_liquido_final': round(montante_liquido, 2)
    }

#Função para exibir os calculos de maneira recursiva
@app.route('/calcular_inv', methods=['POST'])
def calcular():
    data = request.get_json()
    valor_inicial = float(data.get('initialAmount', 0))
    aporte_mensal = float(data.get('monthlyAmount', 0))
    taxa_anual = float(data.get('interestRate', 0))
    periodo = int(data.get('timePeriod', 1))
    tipo_periodo = data.get('timePeriodUnit', 'years')
    tipo_investimento = data.get('investmentType', 'pre')
    tributacao = float(data.get('taxPeriod', 0))

    resultados = calcular_investimento(valor_inicial, aporte_mensal, taxa_anual, periodo, tipo_periodo, tipo_investimento, tributacao)
    return jsonify(resultados)


@app.route('/Riscos', methods=["GET", "POST"])
def riscos():
    return render_template('riscos.html')


if __name__ == '__main__':
    app.run(debug=True)





