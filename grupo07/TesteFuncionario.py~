#encoding:utf-8

import unittest
from should_dsl import should
from ludibrio.stub import Stub
from Funcionario import Funcionario

from bottle import route, install, template, run
from bottle_sqlite import SQLitePlugin

class TesteFuncionario(unittest.TestCase):
    def setUp(self):
        self.func = Funcionario()

    def teste_cadastrar_funcionario_inexistente(self):
        install(SQLitePlugin(dbfile='grupo07/funcionarios.db'))
        dados = {"codigoFuncionario":"0001", "nome":"Filipe", "endereco":"Arantes", "sexo":"m", "datanascimento":"00/00/00"}
        
        self.func.cadastrarFuncionario(db,dados) |should| equal_to(True)
    
#    def teste_cadastrar_funcionario_existente_ou_seja_com_mesmo_codigo(self):
#        dados = {"codigoFuncionario":"0001", "nome":"Filipe", "endereco":"Arantes", "sexo":"m", "datanascimento":"00/00/00"}
#        self.func.cadastrarFuncionario(dados) |should| equal_to(False)
#        
#    def teste_cadastrar_funcionario_com_codigo_nulo(self):
#        dados = {"codigoFuncionario":"", "nome":"Filipe", "endereco":"Arantes", "sexo":"m", "datanascimento":"00/00/00"}
#        self.func.cadastrarFuncionario(dados) |should| equal_to(False)
        
        
