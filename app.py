from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Função para carregar os textos salvos de um arquivo
def load_texts():
    try:
        with open('texts.txt', 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# Função para salvar os textos digitados no arquivo
def save_text(text):
    with open('texts.txt', 'a') as file:
        file.write(text + '\n')

# Lista para armazenar os textos digitados
texts = load_texts()

@app.route('/')
def index():
    return render_template('index.html', texts=texts)

@app.route('/save', methods=['POST'])
def save():
    text = request.form['text']
    save_text(text)
    texts.append(text)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
