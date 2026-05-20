# MedLink

MedLink é uma plataforma web de agendamento de consultas médicas online, desenvolvida para conectar pacientes e médicos de forma simples, moderna e organizada.

O sistema permite visualizar especialidades médicas, encontrar profissionais disponíveis e realizar agendamentos de consultas por meio de uma interface intuitiva.

Este projeto foi desenvolvido como parte da disciplina de **Programação Web** do Centro Universitário Barão de Mauá.

---

# Funcionalidades

## Visitantes

- Visualizar página inicial do sistema
- Visualizar informações sobre a plataforma
- Navegar pelas especialidades médicas disponíveis
- Visualizar médicos cadastrados por especialidade
- Acessar páginas dinâmicas de detalhes das especialidades

## Pacientes

- Cadastro de usuários
- Login e logout
- Agendamento de consultas
- Visualização de consultas agendadas
- Cancelamento e edição de consultas

## Administração

O sistema utiliza o Django Admin para gerenciamento interno.

O administrador pode:

- cadastrar especialidades;
- cadastrar médicos;
- visualizar consultas;
- filtrar consultas por status, médico e data;
- buscar médicos por nome, CRM ou especialidade.

---

# Tecnologias Utilizadas

## Backend

- Python 3.13
- Django 6.0.2
- Django Cotton
- Django Browser Reload
- SQLite
- UV Package Manager

## Frontend

- HTML5
- CSS3
- JavaScript
- Tailwind CSS
- DaisyUI
- Bootstrap Icons

## Versionamento

- Git
- GitHub

---

# Estrutura do Projeto

```text
projeto-web-semestre-medlink/
├── docs/
│   ├── data-model.md
│   └── MedLink.png
├── src/
│   └── med-link/
│       ├── manage.py
│       ├── app/
│       ├── config/
│       ├── templates/
│       ├── static/
│       └── db.sqlite3
└── README.md
```

---

# Modelo de Dados

O sistema utiliza os seguintes models principais:

## Specialty

Representa as especialidades médicas disponíveis no sistema.

## Doctor

Representa os médicos cadastrados, vinculados a uma especialidade e a um usuário do Django.

## Appointment

Representa os agendamentos de consultas entre pacientes e médicos.

---

# Relacionamentos ORM

O projeto utiliza Django ORM com os seguintes relacionamentos:

```text
Specialty 1:N Doctor
Doctor 1:N Appointment
User 1:N Appointment
```

---

# Funcionalidades ORM Implementadas

- Models relacionais
- Migrations
- Django Admin customizado
- Relacionamentos entre entidades
- Queries dinâmicas com ORM
- prefetch_related para otimização de consultas
- Páginas dinâmicas renderizadas com dados do banco

---

# Fixtures

O projeto possui fixtures com dados iniciais para facilitar testes e apresentação.

Incluem:

- especialidades médicas;
- médicos cadastrados;
- usuários médicos.

Arquivo:

```text
app/fixtures/initial_data.json
```

Para carregar os dados:

```bash
uv run python manage.py loaddata app/fixtures/initial_data.json
```

---

# Como Executar o Projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/barao-maua/projeto-web-semestre-medlink.git
```

## 2. Entrar na pasta do projeto

```bash
cd projeto-web-semestre-medlink/src/med-link
```

## 3. Instalar dependências

```bash
uv sync
```

## 4. Rodar migrations

```bash
uv run python manage.py migrate
```

## 5. Carregar fixtures

```bash
uv run python manage.py loaddata app/fixtures/initial_data.json
```

## 6. Executar o servidor

```bash
uv run python manage.py runserver
```

---

# Rotas Principais

| Rota | Descrição |
|---|---|
| `/` | Página inicial |
| `/sobre/` | Página sobre |
| `/especialidades/` | Lista de especialidades |
| `/especialidades/<id>/` | Página dinâmica da especialidade |
| `/admin/` | Painel administrativo |

---

# Protótipo

O wireframe do projeto está disponível em:

```text
https://www.figma.com/design/cNwc8MnUpOI1RfR2kMtR0k/Wireframe
```

---

# Documentação

## Modelo de dados

```text
docs/data-model.md
```

## Diagrama entidade-relacionamento

```text
docs/MedLink.png
```

---

# Divisão de Tarefas

## Rafael Avelar

Responsável por:

- Modelagem ORM
- Models do sistema
- Relacionamentos entre entidades
- Configuração do Django Admin
- Fixtures iniciais
- Integração dinâmica das especialidades
- Rotas dinâmicas de especialidades
- Estrutura backend

## Nicole Santarosa

Responsável por:

- Autenticação
- Login e cadastro
- CRUD de agendamentos
- Proteção de rotas
- Fluxo do usuário
- Forms
- Integração das funcionalidades do paciente

---

# Equipe

- Rafael Avelar
- Nicole Santarosa

---

# Objetivo Acadêmico

O projeto tem como objetivo aplicar conceitos de:

- desenvolvimento web;
- ORM;
- autenticação;
- CRUD;
- modelagem de banco de dados;
- renderização server-side;
- componentização;
- controle de versão com Git e GitHub.