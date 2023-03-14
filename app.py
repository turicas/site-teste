from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "Olá, mundo! Esse é meu site. (Álvaro Justen)"

@app.route("/sobre")
def sobre():
  return "Aqui vai o conteúdo da página Sobre"

@app.route("/contato")
def contato():
  return "Aqui vai o conteúdo da página Contato"
