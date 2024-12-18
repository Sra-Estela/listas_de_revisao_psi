from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return "<h1>Bem-vindo ao Flask!</h1>"

@app.route('/sobre')
def sobre():
	return "<h1>Esta é a página Sobre</h1>"

@app.route('/saudacao/<nome>')
def saudacao(nome):
	return f"<h1>Olá, {nome}! Bem-vindo(a) ao Flask!</h1>"

@app.route('/contato/<msg>')
def contato(msg):
	return f"<h1>Sua mensagem é: {msg};</h1>" #Oi