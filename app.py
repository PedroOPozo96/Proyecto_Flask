from flask import Flask, render_template, request, abort
import json 
import os

app = Flask(__name__)

def load_data():
    with open('libros.json', encoding='utf-8') as f:
        return json.load(f)['libros']


libros = load_data()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/libros', methods=['GET', 'POST'])
def libros_view():
    query = request.args.get('q', '')
    resultados = [libro for libro in libros if query.lower() in libro['nombre'].lower()]
    if not resultados:
        abort(404)
    return render_template('libros.html', libros=resultados, query=query)

@app.route('/libro/<int:libro_id>')
def libro_detalle(libro_id):
    libro = next((libro for libro in libros if libro['id'] == libro_id), None)
    if libro is None:
        abort(404)
    return render_template('libro_detalle.html', libro=libro)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)