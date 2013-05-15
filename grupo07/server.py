#encoding:utf-8

from bottle import route, install, template, run, get, post, request
from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile='funcionarios.db'))

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
def cadasdastrarFuncionario(db):
    codigo = request.forms.get("codigo")
    nome = request.forms.get("nome")
    endereco = request.forms.get("endereco")
    sexo = request.forms.get("sexo")
    datanascimento = request.forms.get("datanascimento")
    
    sql = "SELECT codigoFuncionario FROM funcionarios WHERE codigoFuncionario='%s'" %codigo
    c = db.execute(sql)
    if c.fetchone():
        return "Um funcionário já possui este código!"  
    else:
        sql = "INSERT INTO funcionarios (codigoFuncionario,nome,endereco,sexo,datanascimento) VALUES('%s','%s','%s','%s','%s')" %(codigo,nome,endereco,sexo,datanascimento)
        c = db.execute(sql)
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
def consultarFuncionario(db):
    codigo = request.forms.get("codigo")
    

    c = db.execute('SELECT * FROM funcionarios WHERE codigoFuncionario = ?',(codigo,))
    if c.fetchone():
        f = c.fetchone()
        print f['nome']
        return template("exibirFuncionario", codigoFuncionario=f["codigoFuncionario"], nome=f["nome"], endereco=f["endereco"], sexo=f["sexo"], datanascimento=f["datanascimento"])
#        return template("exibirFuncionario", sql2=sql)
    

#Tela para deletar funcionario
@get("/deletar")    
def formDeletarFuncionario():
    return '''<h1>Deletar Funcinário</h1>
        <form method="POST" action="/deletar">
            Código: <input type="text" name="codigo"><input type="Submit" value="Deletar">
        </form>
    '''

@post("/deletar")
def deletarFuncionario(db):
    codigo = request.forms.get("codigo")
    
    sql = "SELECT * FROM funcionarios WHERE codigoFuncionario='%s'" %codigo
    c = db.execute(sql)
    if c.fetchone():
        sql = "DELETE FROM funcionarios WHERE codigoFuncionario='%s'" %codigo
        c = db.execute(sql)
        return "Funcionário deletado."
    else:
        return "Não há funcinário com este código."


run(host="localhost", port=8007, debug=True)
