from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html', row=8, column=8, color1='black', color2='red')


@app.route('/index/<int:row>/<int:column>')
def tablero(row, column):
    return render_template('index1.html', row=row, column=column, color1='black', color2='red')

@app.route('/index/<int:row>/<int:column>,<string:color1>,<string:color2>')
def colors(row, column, color1, color2):
    return render_template('index1.html', row=row, column=column, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)