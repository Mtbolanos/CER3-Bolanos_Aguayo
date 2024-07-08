from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produccion
from .forms import ProduccionForm
from django.utils import timezone
from django.db.models import Sum
import requests
import json
from django.contrib.auth import login, authenticate
from .forms import RegistroForm

def notificar_slack(mensaje):
    url = 'https://hooks.slack.com/services/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'
    payload = {'text': mensaje}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if response.status_code != 200:
        raise ValueError(f'Request to Slack returned an error {response.status_code}, the response is:\n{response.text}')


@login_required
def registrar_produccion(request):
    if request.method == 'POST':
        form = ProduccionForm(request.POST)
        if form.is_valid():
            produccion = form.save(commit=False)
            produccion.operador = request.user.get_full_name()
            produccion.save()
            # Notificar a Slack
            total_produccion_operador = Produccion.objects.filter(
                operador=produccion.operador,
                anulado=False
            ).aggregate(total=Sum('cantidad'))['total'] or 0
            total_produccion_general = Produccion.objects.filter(
                anulado=False
            ).aggregate(total=Sum('cantidad'))['total'] or 0
            fecha_formateada = produccion.fecha.strftime('%Y-%m-%d %H:%M')
            mensaje = ( 
                f'Nueva producción registrada: {fecha_formateada}  '
                f'{produccion.planta.nombre} - {produccion.operador} - '
                f'{produccion.producto.nombre}  {produccion.cantidad} lts. | '
                f'Total Almacenado por {produccion.operador}: {total_produccion_operador} lts. - '
                f'Total Almacenado: {total_produccion_general} lts.'
            )
            notificar_slack(mensaje)
            return redirect('lista_produccion')
    else:
        form = ProduccionForm()
    return render(request, 'produccion/registrar_produccion.html', {'form': form})

@login_required
def lista_produccion(request):
    es_supervisor = request.user.groups.filter(name='supervisor').exists()
    es_admin = request.user.groups.filter(name='admin').exists()
    if es_supervisor or es_admin:
        producciones = Produccion.objects.filter(anulado=False)
        return render(request, 'produccion/lista_produccion.html', {'producciones': producciones})
    else:
        producciones = Produccion.objects.filter(operador=request.user.get_full_name(), anulado=False)
        return render(request, 'produccion/lista_produccion.html', {'producciones': producciones})

@login_required
def modificar_produccion(request, pk):
    es_supervisor = request.user.groups.filter(name='supervisor').exists()
    es_admin = request.user.groups.filter(name='admin').exists()
    if es_supervisor or es_admin:
        produccion = get_object_or_404(Produccion.objects.all(), pk=pk)
        if request.method == 'POST':
            form = ProduccionForm(request.POST, instance=produccion)
            if form.is_valid():
                form.save()
                return redirect('lista_produccion')
        else:
            form = ProduccionForm(instance=produccion)
        return render(request, 'produccion/modificar_produccion.html', {'form': form})
    else:
        produccion = get_object_or_404(Produccion, pk=pk, operador=request.user.get_full_name())
        if request.method == 'POST':
            form = ProduccionForm(request.POST, instance=produccion)
            if form.is_valid():
                form.save()
                return redirect('lista_produccion')
        else:
            form = ProduccionForm(instance=produccion)
        return render(request, 'produccion/modificar_produccion.html', {'form': form})
    
def home(request):
    title = "Inicio"

    data = {
        "title" : title,
    }

    return render(request, 'home.html',data)

def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Nombre de usuario o contraseña incorrectos.'
            
    return render(request, 'registration/login.html', {'error_message': error_message})