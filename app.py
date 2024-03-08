from flask import Flask
from login import login
from notes import index, save

app = Flask(__name__)

app.secret_key = "LGBSBGKYW#TBRjGJKgkejhrg"



# Rotas para login
app.add_url_rule('/', 'login', login, methods=['GET', 'POST'])

# Rotas para o bloco de notas
app.add_url_rule('/index', 'index', index)
app.add_url_rule('/save', 'save', save, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
