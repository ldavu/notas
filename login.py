# login.py
from flask import request, render_template, redirect, url_for, session
from usuarios import usuarios
from hashlib import sha256

def authenticate(username, password):
    # Combinar o nome de usuário e a senha fornecidos
    # Certifique-se de que a senha seja uma string antes de convertê-la em bytes
    password_bytes = password.encode()
    
    # Calcular o hash da combinação
    input_hash = sha256(username.encode() + password_bytes).hexdigest()
    
    # Verificar se o hash calculado está presente no dicionário de usuários
    if input_hash in usuarios.values():
        return True
    return False

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Autenticar o usuário
        if authenticate(username, password):
            # Se o login for bem-sucedido, redirecionar para a página 'index'
            session["login"]=True
            return redirect(url_for('index'))  # Redirecionar para a página do bloco de notas
        else:
            # Se o login falhar, renderizar a página de login com uma mensagem de erro
            error = f'Usuário ou senha inválidos. Por favor, tente novamente. {username, password}'
            return render_template('login.html', error=error)

    # Se a solicitação for GET ou se o login falhar, renderizar o formulário de login
    return render_template('login.html')
