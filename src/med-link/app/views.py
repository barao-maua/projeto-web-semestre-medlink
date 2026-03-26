# render é a função do Django que junta uma requisição com um template HTML
from django.shortcuts import render

# Função chamada quando o usuário acessa "/"
def index(request):
    # render recebe 3 argumentos:
    # 1. request → a requisição do usuário
    # 2. o caminho do template HTML a ser renderizado
    # 3. um dicionário de contexto → variáveis enviadas para o template
    return render(request, 'pages/index.html', {
        'extra_css': 'css/index.css',  # CSS específico da Home, carregado no base.html
        'extra_js': 'js/index.js',     # JS específico da Home, carregado no base.html
    })

# Função chamada quando o usuário acessa "/sobre/"
def sobre(request):
    return render(request, 'pages/sobre.html', {
        'extra_css': 'css/sobre.css',
        'extra_js': 'js/sobre.js',
    })

# Função chamada quando o usuário acessa "/especialidades/"
def especialidades(request):
    return render(request, 'pages/especialidades.html', {
        'extra_css': 'css/especialidades.css',
        'extra_js': 'js/especialidades.js',
    })