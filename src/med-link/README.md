# Django Starter

Um template starter para projetos Django moderno com configurações otimizadas para desenvolvimento, componentes reutilizáveis e styling moderno.

## Features

- **Django 6.x+** - Framework web Python
- **UV** - Package manager rápido e moderno
- **Django Cotton** - Sistema de componentes reutilizáveis
- **Django Browser Reload** - Auto-reload do navegador durante desenvolvimento
- **Tailwind CSS** - Framework CSS utilitário
- **DaisyUI** - Componentes UI baseados em Tailwind
- **Configurações de Desenvolvimento** - Settings otimizados para dev local

## Tecnologias

### Backend
| Tecnologia | Descrição |
|-----------|-----------|
| Django 6.x | Framework web |
| UV | Package manager |
| Django Cotton | Componentes reutilizáveis |
| Django Browser Reload | Auto reload em desenvolvimento |
| Python 3.10+ | Linguagem base |

### Frontend
| Tecnologia | Descrição |
|-----------|-----------|
| Tailwind CSS | Framework CSS |
| DaisyUI | Componentes UI |
| HTML5 | Markup |

## Instalação

### 1) Clonar o repositório

```bash
git clone <url-do-repositorio>
cd django_starter
```

### 2) Criar ambiente virtual e instalar dependências

**Com UV (recomendado):**

```bash
uv sync
```

**Com pip:**

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3) Executar migrações

```bash
python manage.py migrate
```

### 4) Coletar arquivos estáticos (se necessário)

```bash
python manage.py collectstatic
```

### 5) Rodar servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000/

## Estrutura do Projeto

```
django_starter/
├── manage.py
├── requirements.txt
├── pyproject.toml           # Configuração UV
├── README.md
├── tailwind.config.js       # Config Tailwind + DaisyUI
├── config/                  # Configurações Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── app/                    # App principal
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── admin.py
├── static/                 # Arquivos CSS gerado
│   └── css/
│       └── style.css
├── templates/              # Templates HTML
│   ├── components/        # Cotton components
│       ├── layouts.html
│           ├── base.html
│   └── pages/
└── media/                 # Arquivos de usuários
```

## Comandos 

```bash
# Criar admin
python manage.py createsuperuser

# Fazer migrations
python manage.py makemigrations
python manage.py migrate

# Shell Django
python manage.py shell

# Coletar estáticos
python manage.py collectstatic

# Rodar testes
python manage.py test

```
## Passo a passo realizado para criação do django-starter

Esta seção descreve, em ordem, o processo usado para montar este starter Django, desde a criação do projeto até a organização de templates, componentes e arquivos estáticos.

### 1) Criar o projeto Django

Primeiro foi criado o projeto base com o comando abaixo:

```bash
django-admin startproject config .
```

Esse comando gera a estrutura inicial do Django no diretório atual, incluindo:

- `manage.py`
- pasta `config/`
- `settings.py`, `urls.py`, `wsgi.py` e `asgi.py`

Neste starter, o projeto principal ficou com o nome `config`, o que ajuda a separar melhor as configurações do app da aplicação.

### 2) Criar o app principal

Depois foi criado o app principal do projeto:

```bash
python manage.py startapp app
```

Em seguida, o app foi adicionado em `INSTALLED_APPS` no arquivo `config/settings.py`:

```python
'app.apps.AppConfig',
```

Esse app passou a concentrar as views principais, como a view inicial definida em `app/views.py`.

### 3) Instalar as dependências do starter

As dependências principais foram adicionadas ao projeto para suportar desenvolvimento moderno e componentes reutilizáveis:

```bash
uv add django django-browser-reload django-cotton pillow
```

Ou, alternativamente, com `pip`:

```bash
pip install django django-browser-reload django-cotton pillow
```

As bibliotecas usadas neste projeto são:

- `django`
- `django-browser-reload`
- `django-cotton`
- `pillow`

### 4) Configurar o Django Cotton

Para usar componentes com Django Cotton, foi necessário adicionar o pacote em `INSTALLED_APPS` dentro de `config/settings.py`:

```python
'django_cotton',
```

Também foi definida a pasta onde os componentes serão procurados:

```python
COTTON_DIR = 'components'
```

Com isso, os componentes foram organizados em:

```text
templates/components/
```

Exemplo prático deste projeto:

- `templates/components/header.html`
- `templates/components/layouts/base.html`

No template principal, o layout é usado com a sintaxe do Cotton:

```html
<c-layouts.base>
  ...conteudo da pagina...
</c-layouts.base>
```

E dentro do layout, o conteúdo da página é renderizado com:

```html
{{ slot }}
```

### 5) Configurar a pasta global de templates

Para permitir o uso de templates fora dos apps, foi configurada uma pasta global chamada `templates/` na raiz do projeto.

No arquivo `config/settings.py`, a chave `DIRS` foi ajustada assim:

```python
TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR / 'templates'],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]
```

Essa configuração permite usar arquivos como:

- `templates/index.html`
- `templates/components/header.html`
- `templates/components/layouts/base.html`

### 6) Organizar os templates do projeto

A estrutura de templates foi separada para facilitar reutilização e manutenção:

```text
templates/
├── index.html
└── components/
	├── header.html
	└── layouts/
		└── base.html
```

O papel de cada arquivo ficou assim:

- `index.html`: página inicial renderizada pela view principal
- `header.html`: componente reutilizável de navegação
- `layouts/base.html`: layout base com CSS, bibliotecas frontend e `slot` para conteúdo

### 7) Criar a view e a rota inicial

Foi criada uma view simples para renderizar a página inicial:

```python
from django.shortcuts import render

def index(request):
	return render(request, 'index.html')
```

Depois, a rota principal foi registrada em `config/urls.py`:

```python
path('', views.index, name='index'),
```

Assim, ao acessar a raiz do projeto, o Django entrega o template `index.html`.

### 8) Configurar arquivos estáticos

Para servir CSS, imagens e outros assets durante o desenvolvimento, foi criada a pasta:

```text
static/
├── css/
└── images/
```

No arquivo `config/settings.py`, a configuração ficou assim:

```python
STATIC_URL = 'static/'

STATICFILES_DIRS = [
	BASE_DIR / 'static',
]
```

Com isso, o Django passa a procurar arquivos estáticos dentro da pasta `static/` do projeto.

Exemplos usados neste starter:

- `static/css/styles.css`
- `static/images/django-starter-fig.png`

Nos templates, os arquivos estáticos são carregados com:

```html
{% load static %}
```

E referenciados com:

```html
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
<img src="{% static 'images/django-starter-fig.png' %}" alt="Django Starter">
```

### 9) Configurar arquivos de media

Para preparar o projeto para upload e entrega de arquivos enviados por usuários, também foi definida a configuração de media em `config/settings.py`:

```python
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Isso faz com que os arquivos de upload sejam armazenados na pasta:

```text
media/
```

### 10) Servir arquivos static e media no desenvolvimento

Durante o desenvolvimento local, o Django pode servir arquivos estáticos e de media diretamente pelas URLs configuradas.

Para isso, `config/urls.py` foi ajustado com `static()`:

```python
from django.conf import settings
from django.conf.urls.static import static
```

E ao final de `urlpatterns`:

```python
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

Na prática, essa etapa foi incluída para permitir acesso aos assets e aos uploads durante o desenvolvimento, sem depender de servidor web externo.

### 11) Habilitar auto-reload do navegador

Para melhorar a experiência de desenvolvimento, foi configurado o `django-browser-reload`.

Em `INSTALLED_APPS`:

```python
'django_browser_reload',
```

Em `MIDDLEWARE`:

```python
'django_browser_reload.middleware.BrowserReloadMiddleware',
```

E nas URLs:

```python
path('__reload__/', include('django_browser_reload.urls')),
```

Assim, mudanças feitas em templates e páginas podem ser refletidas com mais rapidez durante o desenvolvimento.

### 12) Criar a base visual do starter

O layout base recebeu integração com Tailwind via CDN, DaisyUI e Bootstrap Icons para acelerar a prototipação visual:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
```

Depois disso, a página inicial foi montada em `templates/index.html`, utilizando:

- layout com Cotton
- imagem servida por `static`
- classes utilitárias do Tailwind
- componentes visuais do DaisyUI

### Resumo do fluxo

Em resumo, a construção deste starter seguiu esta sequência:

1. criar o projeto com `startproject`
2. criar o app principal com `startapp`
3. instalar dependências auxiliares
4. registrar app e bibliotecas em `INSTALLED_APPS`
5. configurar pasta global de templates
6. organizar componentes com Django Cotton
7. configurar `static` e `media` em `settings.py`
8. habilitar o atendimento desses arquivos no desenvolvimento
9. criar a view principal e a rota inicial
10. montar layout e página inicial com Tailwind, DaisyUI e componentes reutilizáveis

Esse processo resulta em um projeto Django inicial já pronto para evolução, com base organizada para páginas, componentes, estilos e arquivos estáticos.

