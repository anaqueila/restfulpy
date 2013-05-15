#encoding:utf-8

from bottle import route, install, template, run, get, post, request
from bottle_sqlite import SQLitePlugin
from ludibrio import Mock, Dummy

install(SQLitePlugin(dbfile='funcionarios.db',keyword='dbfun'))

#Tela para cadastrar Funcionario
@get("/cadastrar")
def formCadasdastrarFuncionario():
    return '''<h1>Cadastrar Funcionário</h1>
    <form method="POST" action="/cadastrar">
        Código: <input type="text" name="codigo"><br>
        Nome: <input type="text" name="nome"><br>
        Endereço: <input type="text" name="endereco"><br>
        Sexo: <input type="radio" name="sexo" value="m">M | <input type="radio" name="sexo" value="f">F<br>
        Data de Nascimento: <input type="text" name="datanascimento"><br>
        <input type="Submit" value="Cadastrar">
    </form>'''

#Cadastrar funcinario    
@post("/cadastrar")
def cadasdastrarFuncionario(dbfun):
    codigo = request.forms.get("codigo")
    nome = request.forms.get("nome")
    endereco = request.forms.get("endereco")
    sexo = request.forms.get("sexo")
    datanascimento = request.forms.get("datanascimento")
    
    sql = "SELECT codigoFuncionario FROM funcionarios WHERE codigoFuncionario='%s'" %codigo
    c = dbfun.execute(sql)
    if c.fetchone():
        return "Um funcionário já possui este código!"  
    else:
        sql = "INSERT INTO funcionarios (codigoFuncionario,nome,endereco,sexo,datanascimento) VALUES('%s','%s','%s','%s','%s')" %(codigo,nome,endereco,sexo,datanascimento)
        c = dbfun.execute(sql)
        return "Funcionário cadastrado!"
        
#Tela para consultar funcionario        
@get("/consultar")
def formConsultarFuncionario():
    return '''<h1>Consultar Funcinário</h1>
        <form method="POST" action="/consultar">
            Código: <input type="text" name="codigo"><input type="Submit" value="Consultar">
        </form>
    '''

#Consultar funcionario  
@post("/consultar")
def consultarFuncionario(dbfun):
    codigo = request.forms.get("codigo")

    sql = 'SELECT * FROM funcionarios WHERE codigoFuncionario = "%s"' %codigo
    c = dbfun.execute(sql)
    fun = c.fetchone()
    if fun:
        return template('exibirFuncionario', codigoFuncionario=fun['codigoFuncionario'], nome=fun['nome'], endereco=fun['endereco'], sexo=fun['sexo'], datanascimento=fun['datanascimento'])
    else:
        return "Não há funcinário com este código."
    

#Tela para deletar funcionario
@get("/deletar")    
def formDeletarFuncionario():
    return '''<h1>Deletar Funcinário</h1>
        <form method="POST" action="/deletar">
            Código: <input type="text" name="codigo"><input type="Submit" value="Deletar">
        </form>
    '''

@post("/deletar")
def deletarFuncionario(dbfun):
    codigo = request.forms.get("codigo")
#    
#    sql = "SELECT * FROM funcionarios WHERE codigoFuncionario='%s'" %codigo
#    c = dbfun.execute(sql)
#    if c.fetchone():
#        sql = "DELETE FROM funcionarios WHERE codigoFuncionario='%s'" %codigo
#        c = dbfun.execute(sql)
#        return "Funcionário deletado."
#    else:
#        return "Não há funcinário com este código."


run(host="localhost", port=8007, debug=True)
