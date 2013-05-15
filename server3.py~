from bottle import route, install, template, run
from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile='rest.db'))

@route('/show/<post_id:int>')
def show(db, post_id):
    c = db.execute('SELECT usuario, password FROM alunos WHERE id = ?', (post_id,))
   
    row = c.fetchone()
    print row['usuario']
    return template('show_post', usuario=row['usuario'], password=row['password'])

run(reloader=True, debug=True, host="localhost", port=8007)
