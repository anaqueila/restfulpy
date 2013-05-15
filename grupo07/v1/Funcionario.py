#encoding:utf-8

class Funcionario(object):
#    def __init__(self,db):
#        self.db = db

    def cadastrarFuncionario(self,db,dados):
        sql = "INSERT INTO funcionarios VALUES(NULL,%s,%s,%s,%s,%s)" %(dados["codigoFuncionario"], dados["nome"], dados["endereco"], dados["sexo"], dados["datanascimento"])
        c = db.execute(sql)
        if c.fetchone():
            return True
        else:
            return False     
        
    def consultarFuncionario(self):
        return "consultar"
        
    def deletarFuncionario(self):
        return "deletar"
        
    
