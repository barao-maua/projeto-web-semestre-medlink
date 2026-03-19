from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html', {
        'extra_css': 'css/index.css',
        'extra_js': 'js/index.js',
    })

def sobre(request):
    return render(request, 'pages/sobre.html', {
        'extra_css': 'css/sobre.css',
        'extra_js': 'js/sobre.js',
    })

def especialidades(request):
    return render(request, 'pages/especialidades.html', {
        'extra_css': 'css/especialidades.css',
        'extra_js': 'js/especialidades.js',
    })