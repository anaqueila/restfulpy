#encoding:utf-8

from bottle import route,run,template
import bottle.ext.sqlite

app = bottle.Bottle()
plugin = bottle.ext.sqlite.Plugin(dbfile='funcionarios.db')
app.install(plugin)

@route("/teste")
def teste(db):
    c = db.execute('SELECT * FROM funcionarios')
    row = c.tfetchone()
    print row["nome"]
    return template("show_post", usuario=row["nome"])
    
run(host="localhost", port=8007, debug=True)
