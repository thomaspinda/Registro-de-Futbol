from django import forms
from .models import Equipo, Jugador, Pais

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'pais', 'entrenador', 'escudo']

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'edad', 'posicion', 'pais', 'equipo', 'foto']