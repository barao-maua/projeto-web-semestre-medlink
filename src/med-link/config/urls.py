# Importa o módulo admin do Django (painel administrativo padrão)
from django.contrib import admin

# path → define uma rota | include → inclui rotas de outro arquivo
from django.urls import path, include

# settings → acessa as configurações do projeto (settings.py)
from django.conf import settings

# permite servir arquivos estáticos e de media durante o desenvolvimento
from django.conf.urls.static import static

# importa todas as funções do views.py do app
from app import views

urlpatterns = [
    # Rota raiz "/" → chama views.index → name='index' é o apelido usado no HTML com {% url 'index' %}
    path('', views.index, name='index'),

    # Rota "/sobre/" → chama views.sobre
    path('sobre/', views.sobre, name='sobre'),

    # Rota "/especialidades/" → chama views.especialidades
    path('especialidades/', views.especialidades, name='especialidades'),

    # Rota do painel admin do Django → /admin/
    path('admin/', admin.site.urls),

    # Rota do django-browser-reload → faz o navegador recarregar automaticamente durante o desenvolvimento
    path('__reload__/', include('django_browser_reload.urls')),

# Adiciona as rotas para servir arquivos de media e static durante o desenvolvimento
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)