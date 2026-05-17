# Importa o model User padrão do Django
from django.conf import settings

# Importa os recursos de modelagem do banco de dados
from django.db import models


# Model que representa as especialidades médicas disponíveis no sistema
class Specialty(models.Model):

    # Nome da especialidade
    # unique=True impede especialidades duplicadas
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nome"
    )

    # Descrição opcional da especialidade
    description = models.TextField(
        verbose_name="Descrição",
        blank=True
    )

    class Meta:
        # Nome exibido no Django Admin
        verbose_name = "Especialidade"
        verbose_name_plural = "Especialidades"

        # Ordena as especialidades alfabeticamente
        ordering = ["name"]

    # Define como a especialidade será exibida no sistema
    def __str__(self):
        return self.name


# Model que representa um médico dentro do sistema
class Doctor(models.Model):

    # Relaciona o médico a um usuário do Django
    # OneToOneField significa:
    # um usuário possui apenas um perfil médico
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="doctor_profile",
        verbose_name="Usuário"
    )

    # Especialidade do médico
    # Uma especialidade pode possuir vários médicos
    specialty = models.ForeignKey(
        Specialty,
        on_delete=models.PROTECT,
        related_name="doctors",
        verbose_name="Especialidade"
    )

    # CRM do médico
    # unique=True impede CRMs repetidos
    crm = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="CRM"
    )

    # Descrição profissional do médico
    description = models.TextField(
        verbose_name="Descrição",
        blank=True
    )

    class Meta:
        # Nome exibido no Django Admin
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"

        # Ordena os médicos pelo nome
        ordering = ["user__first_name", "user__last_name"]

    # Define como o médico será exibido no sistema
    def __str__(self):
        full_name = self.user.get_full_name() or self.user.username
        return f"Dr(a). {full_name} - {self.specialty.name}"


# Model que representa um agendamento de consulta
class Appointment(models.Model):

    # Lista de status possíveis do agendamento
    STATUS_CHOICES = [
        ("scheduled", "Agendada"),
        ("completed", "Concluída"),
        ("cancelled", "Cancelada"),
    ]

    # Usuário paciente que realizou o agendamento
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="appointments",
        verbose_name="Paciente"
    )

    # Médico relacionado ao agendamento
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.PROTECT,
        related_name="appointments",
        verbose_name="Médico"
    )

    # Data da consulta
    date = models.DateField(
        verbose_name="Data"
    )

    # Horário da consulta
    time = models.TimeField(
        verbose_name="Horário"
    )

    # Status atual da consulta
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="scheduled",
        verbose_name="Status"
    )

    # Observações opcionais da consulta
    notes = models.TextField(
        verbose_name="Observações",
        blank=True
    )

    # Data de criação do agendamento
    # auto_now_add salva automaticamente a data/hora de criação
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em"
    )

    class Meta:
        # Nome exibido no Django Admin
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"

        # Ordena por data e horário
        ordering = ["date", "time"]

        # Impede dois agendamentos do mesmo médico no mesmo horário
        unique_together = ["doctor", "date", "time"]

    # Define como o agendamento será exibido no sistema
    def __str__(self):
        patient_name = self.patient.get_full_name() or self.patient.username

        return (
            f"{patient_name} com "
            f"{self.doctor} em "
            f"{self.date} às {self.time}"
        )