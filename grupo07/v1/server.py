#encoding:utf-8

from Funcionario import Funcionario

from bottle import route, install, template, run
from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile='grupo07/funcionarios.db'))

func = Funcionario()

@route("/cadastrar")
def cadasdastrarFuncionario(db):
    dados = {"codigoFuncionario":"0001", "nome":"Filipe", "endereco":"Arantes", "sexo":"m", "datanascimento":"00/00/00"}
    return func.cadastrarFuncionario(db,dados)

@route("/consultar")
def consultarFuncionario():
    return func.consultarFuncionario()

@route("/deletar")    
def deletarFuncionario():
    return func.deletarFuncionario()

run(host="localhost", port=8007, debug=True)
