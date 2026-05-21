from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Specialty, Appointment
from .forms import PatientRegistrationForm, AppointmentForm

# Função chamada quando o usuário acessa "/"
def index(request):
    return render(request, 'pages/index.html', {
        'extra_css': 'css/index.css',
        'extra_js': 'js/index.js',
    })

# Função chamada quando o usuário acessa "/sobre/"
def sobre(request):
    return render(request, 'pages/sobre.html', {
        'extra_css': 'css/sobre.css',
        'extra_js': 'js/sobre.js',
    })

# Função chamada quando o usuário acessa "/especialidades/"
def especialidades(request):
    specialties = Specialty.objects.all()
    return render(request, 'pages/especialidades.html', {
        'specialties': specialties,
        'extra_css': 'css/especialidades.css',
        'extra_js': 'js/especialidades.js',
    })

def especialidade_detalhe(request, specialty_id):
    specialty = get_object_or_404(
        Specialty.objects.prefetch_related("doctors__user"),
        id=specialty_id
    )

    return render(request, 'pages/especialidade-detalhe.html', {
        'extra_css': 'css/especialidade-detalhe.css',
        'specialty': specialty,
    })

def register_view(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = PatientRegistrationForm()
    return render(request, 'pages/register.html', {'form': form})

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
    else:
        form = AuthenticationForm(request)

    # adiciona classes Tailwind/DaisyUI
    for field in form.fields.values():
        field.widget.attrs.update({
            'class': 'input input-bordered w-full focus:outline-none focus:ring-2 focus:ring-primary'
        })

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')

    return render(request, 'pages/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def meus_agendamentos(request):

    # verifica se o usuário é médico
    is_doctor = hasattr(request.user, 'doctor_profile')

    if is_doctor:

        # pega o perfil do médico
        doctor = request.user.doctor_profile

        # busca consultas do médico
        appointments = Appointment.objects.filter(
            doctor=doctor
        ).order_by('date', 'time')

    else:

        # busca consultas do paciente
        appointments = Appointment.objects.filter(
            patient=request.user
        ).order_by('date', 'time')

    return render(request, 'pages/meus-agendamentos.html', {
        'appointments': appointments,
        'is_doctor': is_doctor,
    })

@login_required(login_url='login')
def agendar(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()
            return redirect('meus_agendamentos')
    else:
        form = AppointmentForm()
    return render(request, 'pages/agendar.html', {'form': form})

@login_required(login_url='login')
def editar_agendamento(request, pk):

    appointment = get_object_or_404(Appointment, pk=pk)

    is_doctor = hasattr(request.user, 'doctor_profile')

    # verifica permissão
    if is_doctor:

        if appointment.doctor != request.user.doctor_profile:
            return redirect('meus_agendamentos')

    else:

        if appointment.patient != request.user:
            return redirect('meus_agendamentos')

    if request.method == 'POST':

        form = AppointmentForm(request.POST, instance=appointment)

        if form.is_valid():
            form.save()
            return redirect('meus_agendamentos')

    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'pages/agendar.html', {
        'form': form,
        'edit': True,
        'appointment': appointment
    })

@login_required(login_url='login')
def cancelar_agendamento(request, pk):

    appointment = get_object_or_404(Appointment, pk=pk)

    is_doctor = hasattr(request.user, 'doctor_profile')

    # verifica permissão
    if is_doctor:

        if appointment.doctor != request.user.doctor_profile:
            return redirect('meus_agendamentos')

    else:

        if appointment.patient != request.user:
            return redirect('meus_agendamentos')

    if request.method == 'POST':
        appointment.status = 'cancelled'
        appointment.save()
        return redirect('meus_agendamentos')

    return render(request,
                  'pages/cancelar-agendamento.html',
                  {'appointment': appointment})
