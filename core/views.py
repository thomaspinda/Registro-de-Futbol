# core/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipo, Jugador, Pais, Torneo, EquipoTorneo, Partido # Asegúrate de importar todos los modelos necesarios
from .forms import EquipoForm, JugadorForm

from rest_framework import viewsets
from .serializers import (
    PaisSerializer, EquipoSerializer, TorneoSerializer,
    EquipoTorneoSerializer, JugadorSerializer, PartidoSerializer
)

def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'core/lista_equipos.html', {'equipos': equipos})

def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_equipos')
    else:
        form = EquipoForm()
    return render(request, 'core/form_equipo.html', {'form': form, 'accion': 'Crear'})

def editar_equipo(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('lista_equipos')
    else:
        form = EquipoForm(instance=equipo)
    return render(request, 'core/form_equipo.html', {'form': form, 'accion': 'Editar'})

def eliminar_equipo(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    if request.method == 'POST':
        equipo.delete()
        return redirect('lista_equipos')
    return render(request, 'core/confirmar_eliminacion.html', {'objeto': equipo, 'tipo': 'equipo'})


def lista_jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'core/lista_jugadores.html', {'jugadores': jugadores})

def crear_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_jugadores')
    else:
        form = JugadorForm()
    return render(request, 'core/form_jugador.html', {'form': form, 'accion': 'Crear'})

def editar_jugador(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk)
    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect('lista_jugadores')
    else:
        form = JugadorForm(instance=jugador)
    return render(request, 'core/form_jugador.html', {'form': form, 'accion': 'Editar'})

def eliminar_jugador(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk)
    if request.method == 'POST':
        jugador.delete()
        return redirect('lista_jugadores')
    return render(request, 'core/confirmar_eliminacion.html', {'objeto': jugador, 'tipo': 'jugador'})


class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

class EquipoAPIViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

class TorneoViewSet(viewsets.ModelViewSet):
    queryset = Torneo.objects.all()
    serializer_class = TorneoSerializer

class EquipoTorneoViewSet(viewsets.ModelViewSet):
    queryset = EquipoTorneo.objects.all()
    serializer_class = EquipoTorneoSerializer

class JugadorAPIViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

class PartidoViewSet(viewsets.ModelViewSet):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer