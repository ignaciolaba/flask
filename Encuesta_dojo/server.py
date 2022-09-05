from crypt import methods
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    print(request.form)
    Nombre = request.form['nombre']
    Dojo = request.form['dojo']
    Lenguaje = request.form['lenguaje']
    Comentario = request.form['comentario']
    return render_template('result.html', Nombre = Nombre, Dojo=Dojo, Lenguaje = Lenguaje, Comentario = Comentario)

if __name__ == '__main__':
     app.run(debug=True)