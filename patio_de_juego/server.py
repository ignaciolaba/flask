from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ruta():
    return render_template('index.html')

@app.route('/play')
def play():
    return render_template('index.html')*3

@app.route('/play/<int:num>')
def numero(num):
    return render_template('index.html', num=num)

@app.route('/play/<int:num>/<string:color>')
def color(num,color):
    return render_template('index.html', color=color, num = num)

if __name__ == "__main__":
    app.run(debug=True)