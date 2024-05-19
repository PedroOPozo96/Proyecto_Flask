from flask import Flask, render_template, request, redirect, url_for, abort, jsonify
import json

app = Flask(__name__)

# Cargar los datos del archivo JSON
def load_data():
    with open('libros.json', 'r') as file:
        return json.load(file)['libros']

libros = load_data()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/libros', methods=['GET', 'POST'])
def libros_view():
    if request.method == 'POST':
        search_query = request.form.get('search', '').lower()
        filtered_libros = [libro for libro in libros if search_query in libro['nombre'].lower()]
    else:
        filtered_libros = libros
    return render_template('libros.html', libros=filtered_libros)

@app.route('/libro/<int:libro_id>')
def libro_detalle(libro_id):
    libro = next((libro for libro in libros if libro["id"] == libro_id), None)
    if libro is None:
        abort(404)
    return render_template('libro_detalle.html', libro=libro)

if __name__ == '__main__':
    app.run(debug=True)


app.run("0.0.0.0",30000,debug=True)
