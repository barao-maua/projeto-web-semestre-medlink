from django.contrib import admin

# Importa os models que serão gerenciados pelo painel administrativo do Django
from .models import Appointment, Doctor, Specialty


# Configuração do Admin para o model Specialty
@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    # Colunas exibidas na listagem de especialidades
    list_display = ["name", "description"]

    # Permite buscar especialidades pelo nome
    search_fields = ["name"]

    # Ordena as especialidades pelo nome
    ordering = ["name"]


# Configuração do Admin para o model Doctor
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    # Colunas exibidas na listagem de médicos
    list_display = ["get_doctor_name", "crm", "specialty"]

    # Cria filtro lateral por especialidade
    list_filter = ["specialty"]

    # Permite buscar médicos por nome, username, CRM ou especialidade
    search_fields = [
        "user__first_name",
        "user__last_name",
        "user__username",
        "crm",
        "specialty__name",
    ]

    # Ordena os médicos pelo nome do usuário vinculado
    ordering = ["user__first_name", "user__last_name"]

    # Método auxiliar para exibir o nome completo do médico
    @admin.display(description="Médico")
    def get_doctor_name(self, obj):
        return obj.user.get_full_name() or obj.user.username


# Configuração do Admin para o model Appointment
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    # Colunas exibidas na listagem de agendamentos
    list_display = [
        "get_patient_name",
        "doctor",
        "date",
        "time",
        "status",
        "created_at",
    ]

    # Cria filtros laterais para facilitar a busca por status, médico e data
    list_filter = ["status", "doctor", "date"]

    # Permite buscar agendamentos pelo paciente, médico ou CRM do médico
    search_fields = [
        "patient__first_name",
        "patient__last_name",
        "patient__username",
        "doctor__user__first_name",
        "doctor__user__last_name",
        "doctor__user__username",
        "doctor__crm",
    ]

    # Ordena os agendamentos por data e horário
    ordering = ["date", "time"]

    # Campo criado automaticamente, por isso fica apenas como leitura
    readonly_fields = ["created_at"]

    # Método auxiliar para exibir o nome completo do paciente
    @admin.display(description="Paciente")
    def get_patient_name(self, obj):
        return obj.patient.get_full_name() or obj.patient.username