#encoding:utf-8

from Funcionario import Funcionario

from bottle import route,run,template
import bottle.ext.sqlite

app = bottle.Bottle()
plugin = bottle.ext.sqlite.Plugin(dbfile='funcionarios.db')
app.install(plugin)

func = Funcionario()

@route("/cadastrar")
def cadasdastrarFuncionario():
    return func.cadastrarFuncionario()

@route("/consultar")
def consultarFuncionario():
    return func.consultarFuncionario()

@route("/deletar")    
def deletarFuncionario():
    return func.deletarFuncionario()

run(host="localhost", port=8007, debug=True)
