from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/redirecionar')
def redirecionar():
    return redirect(url_for('home'))

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/perfil/<nome>')
def perfil(nome):
    if nome.lower() == "anônimo":
        return redirect(url_for('home'))
    return f"Olá, {nome}! Bem-Vindo(a) ao seu perfil."