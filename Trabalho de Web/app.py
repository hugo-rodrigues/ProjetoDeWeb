from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, make_response,after_this_request

import requests

app = Flask(__name__)


#t1= ts.turno1 
#t2= ts.turno2 
#t3= ts.turno3

# rotulosTurno = [ 'Manha', 'Tarde','Noite']


perfil = 0

r = requests.get('https://api.hgbrasil.com/finance')
  
json_object = r.json()
dolarCompra = json_object['results']['currencies']['USD']['buy']
dolarVenda = json_object['results']['currencies']['USD']['sell']
dolarVariacao = json_object['results']['currencies']['USD']['variation']

euroCompra = json_object['results']['currencies']['EUR']['buy']
euroVenda = json_object['results']['currencies']['EUR']['sell']
euroVariacao = json_object['results']['currencies']['EUR']['variation']

loginPrincipal = 'login'
senhaPrincipal = 'senha'
emailPrincipal = 'email@email.com'

loginSecundario = ''
senhaSecundario = ''
emailSecundario = ''


@app.route("/LoginServico", methods=["POST"])
def LoginServico():

    req = request.get_json()

    
   
    
    if req['login'] == loginPrincipal and req['senha'] == senhaPrincipal:
        perfil = 0
        res = make_response(jsonify(req), 200)
    else:  
        if req['login'] == loginSecundario and req['senha'] == senhaPrincipal:
            perfil = 1
            res = make_response(jsonify(req), 200)
         
        else:
            res = make_response(jsonify({"message": "erro"}), 300)
            
    
    return res



@app.route("/cadastrar", methods=["POST"])
def cadastrar():

    req = request.get_json()
    res = make_response(jsonify({"message": "OK"}), 200)

    global  loginSecundario 
    global  senhaSecundario 
    global  emailSecundario 
    loginSecundario = req['usuario']
    senhaSecundario = req['senha']
    emailSecundario = req['email']
    

    print(loginSecundario,senhaSecundario,emailSecundario)
    return res



@app.route("/EditarDados", methods=["POST"])
def MudarDados():
    
    global  loginSecundario 
    global  senhaSecundario 
    global  emailSecundario 
    global  loginPrincipal
    global  senhaPrincipal
    global  emailPrincipal
    req = request.get_json()
    if perfil == 1:
        loginSecundario = req['usuario']
        senhaSecundario = req['senha']
        emailSecundario = req['email']
        res = make_response(jsonify({"message": "OK"}), 200) 
    else:
        loginPrincipal = req['usuario']
        senhaPrincipal = req['senha']
        emailPrincipal = req['email']
        print(emailPrincipal,senhaPrincipal,loginPrincipal,req['email'])
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
        jsonResp = {'login': loginPrincipal , 'senha':senhaPrincipal,'email':emailPrincipal}
      
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
def Pagina_Euro():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    jsonResp = {'euroVariacao': euroVariacao , 'euroCompra':euroCompra}
    return jsonify(jsonResp)

# Index
@app.route('/home')
def index():
    
    return render_template('Home.html',dolarCompra=dolarCompra,dolarVenda=dolarVenda,euroCompra =euroCompra, euroVenda=euroVenda )
        

@app.route('/Dolar')

def Dolar():
    return render_template('Dolar.html')

@app.route('/Euro')

def Euro():
    return render_template('Euro.html')

@app.route('/login')
@app.route('/')
def Login():
    return render_template('Login.html')

@app.route('/cadastro')
@app.route('/cadastro?')
def Cadastro():
    return render_template('Cadastro.html')

@app.route('/servico')

def Servico():
    return render_template('Servico.html')


@app.route('/sobre')

def Sobre():
    return render_template('Sobre.html')

@app.route('/perfil')
@app.route('/perfil?')
def Perfil():
    
    return render_template('Perfil.html',)

if __name__ == '__main__':

    app.run(debug=True)
