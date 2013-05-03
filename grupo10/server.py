from bottle import route, install, template, run, post, request
from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile="contas_receber.db"))

@route('/conta-a-receber')
def contaAReceber():
    return template('conta_receber_form')
    
@post('/conta-a-receber')
def contaAReceberPost(db):
    codigoAreceber = request.forms.get('codigoContaAReceber')
    codigoVenda    = request.forms.get('codigoVenda')
    dataVencimento = request.forms.get('dataVencimento')
    dataPagamento  = request.forms.get('dataPagamento')
    status         = request.forms.get('status')
    
    ret = db.execute("INSERT INTO conta_receber (id_conta_receber, id_venda, data_vencimento, data_pagamento, status) values ('%s', '%s', '%s', '%s', '%s')"%(codigoAreceber, codigoVenda, dataVencimento, dataPagamento, status))
    return "Sucesso eh o que nos espera"
    
@route('/existe-conta-a-receber-por-cod-venda/<idVenda>')
def getContaAReceber(db, idVenda):
    retorno = db.execute("SELECT * FROM conta_receber WHERE id_venda = ?", (idVenda,))
    row = retorno.fetchone()
    if row == None:
        return 'False'
    else:
        return 'True'
        
@route('/conta-a-receber/<idContaReceber>')
def getContaAReceber(db, idContaReceber):
    retorno = db.execute("SELECT * FROM conta_receber WHERE id_conta_receber = ?", (idContaReceber,))
    row = retorno.fetchone()
    if row == None:
        return 'Conta com o id %s nao foi encontrada'%(idContaReceber)
    else:
        return {'codigoAreceber':row['id_conta_receber'],'codigoVenda':row['id_venda'],'dataVencimento':row['data_vencimento'],'dataPagamento':row['data_pagamento'],'status':row['status']}
        
@route('/apagar-conta-a-receber/<idContaReceber>')
def apagarContaAReceber(db, idContaReceber):
    retorno = db.execute("SELECT * FROM conta_receber WHERE id_conta_receber = ?", (idContaReceber,))
    row = retorno.fetchone()
    if row == None:
        return 'Conta inexistente'
    
    db.execute("DELETE FROM conta_receber WHERE id_conta_receber = ?", (idContaReceber,))
    return "Removido com sucesso"

run(host='localhost', port=9090, debug=True)
