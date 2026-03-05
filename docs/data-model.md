# Modelo de Dados - MedLink

## Visão Geral

O sistema MedLink é uma plataforma web para gerenciamento de consultas médicas online.  
O modelo de dados foi projetado para permitir o cadastro de usuários, gerenciamento de médicos e especialidades, além do agendamento de consultas entre pacientes e profissionais de saúde.

O modelo utiliza quatro entidades principais:

- User
- Doctor
- Specialty
- Appointment

Cada entidade representa um componente essencial do funcionamento do sistema.

---

# Entidades do Sistema

## 1. User

A entidade **User** representa todos os usuários cadastrados no sistema.  
Ela armazena as informações básicas necessárias para identificação e autenticação dentro da plataforma.

Usuários podem assumir diferentes papéis dentro da aplicação, como pacientes ou médicos. Pacientes utilizam a plataforma para buscar profissionais e agendar consultas, enquanto médicos possuem informações adicionais armazenadas na entidade Doctor.

Essa entidade é fundamental para o funcionamento do sistema, pois todas as interações da plataforma dependem de um usuário autenticado.

### Atributos

| Campo | Tipo | Descrição |
|-----|-----|-----|
| id | PK | Identificador único do usuário |
| first_name | string | Nome do usuário |
| last_name | string | Sobrenome do usuário |
| email | string | Email utilizado para login |
| password | string | Senha criptografada do usuário |
| phone | string | Número de telefone |
| role | string | Tipo de usuário (paciente ou médico) |
| created_at | datetime | Data de criação da conta |

---

## 2. Doctor

A entidade **Doctor** representa os médicos cadastrados na plataforma.

Ela armazena informações profissionais adicionais relacionadas aos usuários que possuem papel de médico no sistema. Cada médico está associado a um usuário da plataforma, permitindo separar os dados pessoais dos dados profissionais.

Além disso, cada médico está associado a uma especialidade médica, permitindo que pacientes encontrem profissionais de acordo com suas necessidades.

### Atributos

| Campo | Tipo | Descrição |
|-----|-----|-----|
| id | PK | Identificador do médico |
| user_id | FK | Referência ao usuário correspondente |
| specialty_id | FK | Especialidade médica do profissional |
| crm | string | Número de registro profissional do médico |
| description | text | Descrição ou biografia profissional |

### Chaves

PK: id
FK: user_id → User.id
FK: specialty_id → Specialty.id

---

## 3. Specialty

A entidade **Specialty** representa as especialidades médicas disponíveis no sistema.

Seu objetivo é organizar os médicos de acordo com suas áreas de atuação, como cardiologia, dermatologia, pediatria, entre outras. Essa estrutura permite que os pacientes filtrem ou busquem profissionais com base na especialidade desejada.

Uma especialidade pode estar associada a vários médicos diferentes.

### Atributos

| Campo | Tipo | Descrição |
|-----|-----|-----|
| id | PK | Identificador da especialidade |
| name | string | Nome da especialidade médica |
| description | text | Descrição da especialidade |

### Chaves

PK: id

---

## 4. Appointment

A entidade **Appointment** representa os agendamentos de consultas médicas realizados na plataforma.

Cada registro dessa entidade conecta um paciente a um médico em uma data e horário específicos. Além disso, a consulta possui um status que indica se ela está agendada, cancelada ou concluída.

Essa entidade é responsável por registrar e gerenciar todas as consultas realizadas dentro do sistema.

### Atributos

| Campo | Tipo | Descrição |
|-----|-----|-----|
| id | PK | Identificador da consulta |
| patient_id | FK | Usuário que realizou o agendamento |
| doctor_id | FK | Médico responsável pela consulta |
| date | date | Data da consulta |
| time | time | Horário da consulta |
| status | string | Status da consulta (agendada, cancelada, concluída) |
| notes | text | Observações adicionais |

### Chaves

PK: id
FK: patient_id → User.id
FK: doctor_id → Doctor.id

---

# Relacionamentos entre Entidades

O modelo de dados estabelece diferentes relacionamentos entre as entidades para representar corretamente o funcionamento do sistema.

## User → Doctor

Relacionamento **1:1**

Cada médico do sistema está associado a um usuário da plataforma.

Doctor.user_id → User.id

Isso significa que um médico é um usuário que possui informações profissionais adicionais.

---

## Specialty → Doctor

Relacionamento **1:N**

Uma especialidade médica pode estar associada a vários médicos.

Doctor.specialty_id → Specialty.id

Cada médico possui apenas uma especialidade principal.

---

## User → Appointment

Relacionamento **1:N**

Um usuário (paciente) pode agendar várias consultas médicas ao longo do tempo.

Appointment.patient_id → User.id

---

## Doctor → Appointment

Relacionamento **1:N**

Um médico pode possuir várias consultas agendadas com diferentes pacientes.

Appointment.doctor_id → Doctor.id

---

# Resumo do Modelo

O modelo de dados foi projetado para permitir:

- Cadastro de usuários na plataforma
- Identificação de médicos e suas especialidades
- Agendamento de consultas médicas
- Organização das consultas realizadas

As quatro entidades principais do sistema são:

- **User**
- **Doctor**
- **Specialty**
- **Appointment**

Essas entidades e seus relacionamentos formam a base estrutural para o funcionamento da plataforma MedLink.