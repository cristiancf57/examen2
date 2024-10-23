from flask import Flask,render_template,redirect,session,request,url_for

app = Flask(__name__)
app.secret_key = 'clavesecreta'

@app.route('/')
def index():
    estudiante = "CRISTIAN HUMBERTO FLORES CASTILLO"
    ci = "9166669"
    if 'lista' not in session:
        session['lista']=[]
    return render_template("index.html",estudiante=estudiante,ci=ci,lista = session['lista'])

@app.route('/procesa',methods=['GET','POST'])
def procesa():
    nombre = request.form.get('nombre')
    cantidad = request.form.get('cantidad')
    precio = request.form.get('precio')
    categoria = request.form.get('categoria')
    fecha = request.form.get('fecha')
    if 'lista' not in session:
        session['lista'] = []

    # diccionario de datos
    nuevo={
        'nombre':nombre,
        'cantidad':cantidad,
        'precio':precio,
        'categoria':categoria,
        'fecha':fecha
    }
    # agregar el inscrito a la session
    session['lista'].append(nuevo)
    session.modified=True
    return redirect(url_for('index'))

@app.route('/agregar')
def agregar():
    return render_template('agregar.html')

@app.route('/editar')
def editar():
    nombre = request.args.get('nombre')
    cantidad = request.args.get('cantidad')
    precio = request.args.get('precio')
    categoria = request.args.get('categoria')
    fecha = request.args.get('fecha')
    return render_template('editar.html',nombre= nombre,cantidad=cantidad,precio=precio,categoria=categoria,fecha=fecha)

@app.route('/eliminar')
def eliminar():
    item = request.args.get('item')
    lista = session['lista']
    if 'lista' in session :
        lista.remove(item)
        session['lista'] = lista
    return redirect(url_for('lista'))

@app.route('/vaciar')
def vaciar():
    session.pop('lista',None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)