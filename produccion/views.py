from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Produccion
from .forms import ProduccionForm
from django.utils import timezone
import requests
import json
from django.contrib.auth import login
from .forms import RegistroForm
from django.shortcuts import render, redirect, get_object_or_404

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_produccion')
    else:
        form = RegistroForm()
    return render(request, 'produccion/registro.html', {'form': form})


def notificar_slack(mensaje):
    url = 'https://hooks.slack.com/services/TU_CANAL/WEBHOOK_URL'
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
            produccion.operador = request.user
            produccion.save()
            # Notificar a Slack
            mensaje = f'Nueva producción registrada: Planta {produccion.producto.planta.nombre}, Producto {produccion.producto.nombre}, Litros {produccion.litros}, Fecha {produccion.fecha}, Turno {produccion.turno}'
            notificar_slack(mensaje)
            return redirect('lista_produccion')
    else:
        form = ProduccionForm()
    return render(request, 'produccion/registrar_produccion.html', {'form': form})

@login_required
def modificar_produccion(request, pk):
    produccion = get_object_or_404(Produccion, pk=pk, operador=request.user)
    if request.method == 'POST':
        form = ProduccionForm(request.POST, instance=produccion)
        if form.is_valid():
            form.save()
            return redirect('lista_produccion')
    else:
        form = ProduccionForm(instance=produccion)
    return render(request, 'produccion/modificar_produccion.html', {'form': form})

@login_required
def lista_produccion(request):
    producciones = Produccion.objects.filter(operador=request.user)
    return render(request, 'produccion/lista_produccion.html', {'producciones': producciones})