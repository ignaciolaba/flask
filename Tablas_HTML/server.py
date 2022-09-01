from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ruta():
    return render_template('index2.html')

@app.route('/list')
def render_list():

    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

    return render_template('list.html', random_numbers = [3,1,5], usuarios = users)



if __name__ == "__main__":
    app.run(debug=True)