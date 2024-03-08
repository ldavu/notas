from flask import request, jsonify, render_template

# Função para carregar os textos salvos de um arquivo
def load_texts():
    try:
        with open('shared_text.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ""

# Função para salvar o texto digitado no arquivo
def save_text(text):
    with open('shared_text.txt', 'w') as file:
        file.write(text)

def index():
    shared_text = load_texts()  # Carregar o texto
    return render_template('index.html', shared_text=shared_text)

def save():
    try:
        text = request.json['text']
        text = text.replace('<br>', '\n')  # Substituir <br> por quebras de linha
        save_text(text)
        return jsonify(success=True)
    except Exception as e:
        print(e)
        return jsonify(success=False)
