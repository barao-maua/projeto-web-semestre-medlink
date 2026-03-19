# AGENTS.md

Guia para assistentes de IA que geram codigo neste projeto Django Starter.

## Objetivo do projeto

Este projeto e um starter didatico para estudantes de graduacao sem experiencia previa em programacao web.

Prioridades:
- Clareza e simplicidade do codigo.
- Curva de aprendizado suave.
- Estrutura pequena e facil de entender.
- Evitar recursos avancados do Django quando nao forem necessarios.

## Stack oficial

- Python + Django.
- Gerenciamento de dependencias com UV como padrao.
- Templates HTML com Django Template Language.
- Componentes com Django Cotton (`templates/components`).
- Estilizacao com Tailwind via CDN + DaisyUI.
- Icones com Bootstrap Icons (CDN).
- Function Based Views (FBV).
- Banco padrao: SQLite.

## Regras obrigatorias para geracao de codigo

1. Use Function Based Views (FBV)
- Criar views em `app/views.py` como funcoes simples.
- Mapear rotas com `path(..., views.nome_da_view, ...)`.
- Nao usar Class Based Views (CBV), ViewSets ou DRF neste starter.

2. Nao usar Django Forms neste projeto-base
- Nao criar `forms.py` para fluxo inicial.
- Para formularios didaticos, usar HTML simples no template e ler `request.POST` na view quando necessario.
- Validacoes devem ser basicas e explicadas de forma objetiva.

3. Manter arquitetura enxuta
- Reutilizar o app `app` existente.
- Evitar criar multiplos apps sem necessidade didatica clara.
- Evitar sinais, middlewares customizados, mixins e camadas complexas.

4. Seguir padrao de templates atual
- Reutilizar layout com Cotton: `<c-layouts.base>...</c-layouts.base>`.
- Colocar componentes reutilizaveis em `templates/components/`.
- Usar `{% load static %}` para CSS, imagens e assets locais.

5. Frontend padrao do starter
- Preferir classes do DaisyUI/Tailwind para UI.
- Manter Bootstrap Icons quando houver icones.
- Nao introduzir bundlers, Node build pipeline ou frameworks JS sem pedido explicito.

6. Dependencias e ambiente
- Sempre priorizar comandos com UV.
- Ao sugerir instalacao, usar `uv add ...`.
- Ao preparar ambiente local, usar `uv sync`.
- Nao substituir UV por outra ferramenta como padrao.

7. Didatica primeiro
- Nomes de funcoes, variaveis e templates devem ser autoexplicativos.
- Evitar "magia" e abreviacoes excessivas.
- Sempre preferir a solucao mais simples que funcione bem.
- Quando adicionar codigo, deixar comentarios curtos apenas quando realmente ajudam iniciantes.

## Convencoes do projeto

- Idioma de interface e conteudo: portugues brasileiro (`pt-br`).
- Timezone: `America/Sao_Paulo`.
- Arquivos estaticos em `static/`.
- Imagens em `static/images/`.
- CSS local em `static/css/styles.css`.
- Template inicial em `templates/index.html`.

## Estrutura esperada para novas features pequenas

Quando criar uma nova pagina simples:

1. Criar funcao FBV em `app/views.py`.
2. Registrar rota em `config/urls.py`.
3. Criar template em `templates/` (ou subpasta simples).
4. Se necessario, extrair partes reutilizaveis para `templates/components/`.
5. Aplicar classes DaisyUI/Tailwind para manter padrao visual.

## O que evitar (a menos que o professor peca)

- Django Forms / ModelForms.
- Class Based Views.
- Django REST Framework.
- Autenticacao complexa e permissao avancada.
- Arquiteturas com alta abstracao para um exemplo inicial.
- Dependencias extras sem justificativa didatica.

## Comandos padrao

```bash
uv sync
uv run manage.py migrate
uv run manage.py runserver
```

Para adicionar dependencia:

```bash
uv add nome-do-pacote
```

## Criterio de qualidade para codigo gerado por IA

Sempre explique suas decisões de modo didático e simples.
Antes de finalizar qualquer geracao, validar:

- O codigo esta simples para iniciantes?
- Usa FBV e nao CBV?
- Evita Forms e recursos avancados desnecessarios?
- Respeita a stack oficial (UV, DaisyUI, Bootstrap Icons, Cotton)?
- Mantem consistencia com a estrutura atual do projeto?

Se a resposta for "nao" para qualquer item, simplifique a implementacao.