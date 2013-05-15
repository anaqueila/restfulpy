# -*- coding: cp1252 -*-

from bottle import route, install, template, run, get, post, request
from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile='comissao.db'))


#Tela para cadastrar Comissao
@get("/calcular")
def formCalcularComissao():       
    return '''<h1>Calcular Comissao</h1>
    <form method="POST" action="/calcular">
        Código: <input type="text" name="codigo"><br>
        Codigo do Funcionario: <input type="text" name="codigoFuncionario"><br>
        Ano: <input type="text" name="ano"><br>
        Mes: <input type="radio" name="mes"<br>        
        <input type="Submit" value="Calcular">
    </form>'''

#Cadastrar comissao    
@post("/calcular")
def consultarComissao(db):
    codigo = request.forms.get("codigo")
    codigoFuncionario = request.forms.get("codigoFuncionario")
    ano = request.forms.get("ano")
    mes = request.forms.get("mes")    
    
    sql = "SELECT codigoFuncionario FROM comissao WHERE codigoFuncionario='%s'" %codigo
    c = db.execute(sql)
    if c.fetchone():
        return "Já existe comissao cadastrada para esse funcionario no ano e mes informados!"  
    else:
        sql = "INSERT INTO comissao (codigoFuncionario,ano,mes) VALUES('%s','%s','%s','%s')" %(codigo,codigoFuncionario,ano,mes)
        c = db.execute(sql)
        return "Comissao cadastrada!"
        
#Tela para consultar comissao        
@get("/consultar")
def formConsultarComissao():
    return '''<h1>Consultar Comissao</h1>
        <form method="POST" action="/consultar">
            Código: <input type="text" name="codigo">
            <input type="Submit" value="Consultar">
        </form>
    '''

#Consultar comissao  
@post("/consultar")
def consultarComissao(db):
    codigo = request.forms.get("codigo")
    
    sql = "SELECT * FROM comissao WHERE codigo='%s'" %codigo
    c = db.execute(sql)
    if c.fetchone():
        f = c.fetchone()
        return template("exibirComissao", codigo=f["codigo"], codigoFuncionario=f["codigoFuncionario"], ano=f["ano"], mes=f["mes"])
    

#Tela para deletar comissao
@get("/deletar")    
def formDeletarComissao():
    return '''<h1>Deletar Comissao</h1>
        <form method="POST" action="/deletar">
            Código: <input type="text" name="codigo">
            <input type="Submit" value="Deletar">
        </form>
    '''

@post("/deletar")
def deletarComissao(db):
    codigo = request.forms.get("codigo")
    
    sql = "SELECT * FROM comissao WHERE codigo='%s'" %codigo
    c = db.execute(sql)
    if c.fetchone():
        sql = "DELETE FROM comissao WHERE codigo='%s'" %codigo
        c = db.execute(sql)
        return "Comissao deletada!"
    else:
        return "Não existe a comissao informada!"


run(host="localhost", port=8011, debug=True)
