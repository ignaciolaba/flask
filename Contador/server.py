from curses import meta
from flask import Flask, redirect, render_template, session, request

app = Flask(__name__)
app.secret_key = 'Ejemplo'

@app.route('/')
def home():
    if 'visita' not in session:
        session['visita'] = 1
    else:
        session['visita'] += 1
    
    return render_template('index.html')

@app.route('/agregar_visita', methods=['POST'])
def agregar_visita():
    print(request.form)
    if request.form['add'] == 'Sumar 2':
        session['visita'] += 1
    elif request.form['add'] == 'resetear':
        session['visita'] = 0
    return redirect('/')


@app.route('/destroy_session')
def detroy():
    session.clear()
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)