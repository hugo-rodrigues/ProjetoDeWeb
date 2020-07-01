from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, make_response,after_this_request

import requests

app = Flask(__name__)


#t1= ts.turno1 
#t2= ts.turno2 
#t3= ts.turno3

# rotulosTurno = [ 'Manha', 'Tarde','Noite']
loginPrincipal = 'login'
senhaPrincipal = 'senha'
emailPrincipal = 'email@email.com'

loginSecundario = ''
senhaSecundario = ''
emailSecundario = ''

perfil = ''

r = requests.get('https://api.hgbrasil.com/finance')
  
json_object = r.json()
dolarCompra = json_object['results']['currencies']['USD']['buy']
dolarVenda = json_object['results']['currencies']['USD']['sell']
dolarVariacao = json_object['results']['currencies']['USD']['variation']

euroCompra = json_object['results']['currencies']['EUR']['buy']
euroVenda = json_object['results']['currencies']['EUR']['sell']
euroVariacao = json_object['results']['currencies']['EUR']['variation']



@app.route("/loginEntrada", methods=["POST"])
def create_entry():

    req = request.get_json()

    if req.usuario == loginPrincipal & req.senha == senhaPrincipal:
        perfil = 0
        res = make_response(jsonify({"message": "OK"}), 200)
    else:
        
        if req.usuario == loginSecundario & req.senha == senhaPrincipal:
            perfil = 1
            res = make_response(jsonify({"message": "OK"}), 200)
        else:
            res = make_response(jsonify({"message": "Erro no login"}), 300)
    return res



@app.route("/cadastrar", methods=["POST"])
def cadastrar():

    req = request.get_json()

    loginSecundario = req.usuario
    senhaSecundario = req.senha
    emailSecundario = req.email
    res = make_response(jsonify({"message": "OK"}), 200)
    return res

@app.route("/EditarDados", methods=["POST"])
def cadastrar():

    req = request.get_json()
    if perfil == 1:
        loginSecundario = req.usuario
        senhaSecundario = req.senha
        emailSecundario = req.email
        res = make_response(jsonify({"message": "OK"}), 200) 
    else:
        loginPrincipal = req.usuario
        senhaPrincipal = req.senha
        emailPrincipal = req.email
        res = make_response(jsonify({"message": "OK"}), 200)
    
    return res

@app.route('/EnviarDadosEditar', methods=['GET'])
def EnviarDados():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    if perfil == 1:
        jsonResp = {'login': loginSecundario , 'senha':senhaSecundario,'email':emailSecundario}
    else:
         jsonResp = {'login': loginPrincipal , 'senha':senhaSecundario,'email':emailSecundario}
    return jsonify(jsonResp)

@app.route('/paginaDolar', methods=['GET'])
def Pagina_Dolar():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    jsonResp = {'dolarVariacao': dolarVariacao , 'dolarCompra':dolarCompra}
    return jsonify(jsonResp)

@app.route('/paginaEuro', methods=['GET'])
def Pagina_Dolar():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    jsonResp = {'euroVariacao': euroVariacao , 'euroCompra':euroCompra}
    return jsonify(jsonResp)

# Index
@app.route('/')
def index():
    
    return render_template('Home.html',dolarCompra=dolarCompra,dolarVenda=dolarVenda,euroCompra =euroCompra, euroVenda=euroVenda )
        

@app.route('/Dolar')

def Dolar():
    return render_template('Dolar.html')



@app.route('/login')

def Login():
    return render_template('Login.html')

@app.route('/cadastro')

def Cadastro():
    return render_template('Cadastro.html')

@app.route('/servico')

def Servico():
    return render_template('Servico.html')


@app.route('/sobre')

def Sobre():
    return render_template('Sobre.html')

@app.route('/perfil')

def Perfil():
    return render_template('Perfil.html')

if __name__ == '__main__':

    app.run(debug=True)
