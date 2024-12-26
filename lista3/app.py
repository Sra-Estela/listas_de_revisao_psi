from flask import Flask, request, render_template, url_for, make_response, jsonify
from bd import Dados

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/resposta', methods=['GET', 'POST'])
def isolar_dados():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        comentario = request.form.get('comentario')
        novo_id = len(Dados) + 1
        novo_coment = {
            'id': novo_id,
            'nome': nome,
            'email': email,
            'comentario': comentario
        }
        Dados.append(novo_coment)
        return render_template('resposta.html', dado=novo_coment)
        # return f'''
        #             Obrigado pelo seu feedback, {nome}!
        #             E-mail Confirmado: {email};
        #             Comentário: {comentario}
        #         ''' 
    return render_template('index.html')