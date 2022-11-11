#importação de biblioteca
#importar biblioteca Flask
from flask import Flask, render_template
app = Flask(__name__)

#definição de rotas para o navegador
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)