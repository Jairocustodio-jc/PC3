from flask import Flask, render_template, request, redirect, session
from dao.DAOAlumno import DAOAlumno

app = Flask(__name__)
app.secret_key = 'your_secret_key'

dao_alumno = DAOAlumno()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = dao_alumno.read(username)
        if user and user[0][3] == password:
            session['username'] = username
            return redirect('/inicio_exitoso')  
        else:
            return render_template('login.html', error='Invalid username or password')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        
        user = dao_alumno.read(username)
        if user:
            return render_template('register.html', error='Username already exists')
        else:
            data = {
                'username': username,
                'nombre': nombre,
                'apellidos': apellidos,
                'clave': password
            }
            dao_alumno.insert(data)
            return redirect('/login')
    
    return render_template('register.html')

@app.route('/inicio_exitoso')
@app.route('/inicio_exitoso')
def inicio_exitoso():
    if 'username' in session:
        username = session['username']
        user = dao_alumno.read(username)
        if user:
            nombre = user[0][1]
            apellidos = user[0][2]
            return render_template('inicio_exitoso.html', nombre=nombre, apellidos=apellidos)
        else:
            return redirect('/login')
    else:
        return redirect('/login')
if __name__ == '__main__':
   app.run(debug=True,host="0.0.0.0")
