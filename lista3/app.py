from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Página Inicial"

@app.route('/formulario', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        nome = request.form.get('nome')
        comentario = request.form.get('comentario')
        return f"Obrigado pelo feedback, {nome}! Comentário recebido: {comentario}"
    return render_template('formulario.html') 