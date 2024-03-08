from flask import request, render_template, redirect, url_for
from usuarios import usuarios
import hashlib

# Função para autenticar o usuário
def authenticate(username, password):
    # Verificar se o usuário existe e se a senha está correta
    if username in usuarios and usuarios[username] == hashlib.sha256(password.encode()).hexdigest():
        return True
    return False

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Autenticar o usuário
        if username in usuarios and usuarios[username] == password:
            # Se o login for bem-sucedido, redirecionar para a página 'index'
            return redirect(url_for('index'))  # Redirecionar para a página do bloco de notas
        else:
            # Se o login falhar, renderizar a página de login com uma mensagem de erro
            error = 'Usuário ou senha inválidos. Por favor, tente novamente.'
            return render_template('login.html', error=error)

    # Se a solicitação for GET ou se o login falhar, renderizar o formulário de login
    return render_template('login.html')
