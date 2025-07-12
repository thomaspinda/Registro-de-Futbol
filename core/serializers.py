from rest_framework import serializers
from .models import Pais, Equipo, Torneo, EquipoTorneo, Jugador, Partido


class JugadorNestedSerializer(serializers.ModelSerializer):
    pais_nombre = serializers.ReadOnlyField(source='pais.nombre')
    class Meta:
        model = Jugador
        fields = ['id', 'nombre','edad', 'posicion', 'pais_nombre', 'foto']

class EquipoNestedSerializer(serializers.ModelSerializer):
    pais_nombre = serializers.ReadOnlyField(source='pais.nombre')
    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'pais_nombre', 'entrenador', 'escudo']

class TorneoNestedSerializer(serializers.ModelSerializer):
    pais_nombre = serializers.ReadOnlyField(source='pais.nombre')
    class Meta:
        model = Torneo
        fields = ['id', 'nombre', 'pais_nombre']

class PaisSerializer(serializers.ModelSerializer):
    equipos = EquipoNestedSerializer(many=True, read_only=True)
    jugadores_por_pais = JugadorNestedSerializer(many=True, read_only=True)
    torneos_en_pais = TorneoNestedSerializer(many=True, read_only=True)

    class Meta:
        model = Pais
        fields = ['id', 'nombre', 'equipos', 'jugadores_por_pais', 'torneos_en_pais']

class EquipoSerializer(serializers.ModelSerializer):
    pais_nombre = serializers.ReadOnlyField(source='pais.nombre')
    jugadores = JugadorNestedSerializer(many=True, read_only=True)

    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'pais', 'pais_nombre', 'entrenador', 'escudo', 'jugadores']

class TorneoSerializer(serializers.ModelSerializer):
    pais_nombre = serializers.ReadOnlyField(source='pais.nombre')
    equipos_participantes = serializers.SerializerMethodField()

    class Meta:
        model = Torneo
        fields = ['id', 'nombre', 'pais', 'pais_nombre', 'equipos_participantes']

    def get_equipos_participantes(self, obj):
        equipos_data = []
        for equipo_torneo in obj.equipotorneo_set.all():
            equipo = equipo_torneo.equipo
            jugadores_count = equipo.jugadores.count()
            equipos_data.append({
                'id': equipo.id,
                'nombre': equipo.nombre,
                'entrenador': equipo.entrenador,
                'escudo': equipo.escudo.url if equipo.escudo else None,
                'cantidad_jugadores': jugadores_count
            })
        return equipos_data

class JugadorSerializer(serializers.ModelSerializer):
    pais_nombre = serializers.ReadOnlyField(source='pais.nombre')
    equipo_nombre = serializers.ReadOnlyField(source='equipo.nombre')

    class Meta:
        model = Jugador
        fields = ['id', 'nombre', 'edad', 'posicion', 'pais', 'pais_nombre', 'equipo', 'equipo_nombre', 'foto']
    def validate(self, data):
        jugador_edad = data.get('jugador_edad')

        if jugador_edad < 12:
            raise serializers.ValidationError("El jugador no puede ser menor a 12 años")
        return data

class PartidoSerializer(serializers.ModelSerializer):
    equipo_local_nombre = serializers.ReadOnlyField(source='equipo_local.nombre')
    equipo_visitante_nombre = serializers.ReadOnlyField(source='equipo_visitante.nombre')
    torneo_nombre = serializers.ReadOnlyField(source='torneo.nombre')

    class Meta:
        model = Partido
        fields = ['id', 'fecha', 'equipo_local', 'equipo_local_nombre', 'equipo_visitante', 'equipo_visitante_nombre', 'torneo', 'torneo_nombre', 'goles_local', 'goles_visitante']

    def validate(self, data):

        equipo_local = data.get('equipo_local')
        equipo_visitante = data.get('equipo_visitante')
        goles_local = data.get('goles_local')
        goles_visitante = data.get('goles_visitante')

        if equipo_local and equipo_visitante and equipo_local == equipo_visitante:
            raise serializers.ValidationError("Un equipo no puede jugar contra sí mismo.")

        if goles_local is not None and goles_local < 0:
            raise serializers.ValidationError({"goles_local": "Los goles no pueden ser un número negativo."})
        
        if goles_visitante is not None and goles_visitante < 0:
            raise serializers.ValidationError({"goles_visitante": "Los goles no pueden ser un número negativo."})

        return data
    
class EquipoTorneoSerializer(serializers.ModelSerializer):
    equipo_nombre = serializers.ReadOnlyField(source='equipo.nombre')
    torneo_nombre = serializers.ReadOnlyField(source='torneo.nombre')
    class Meta:
        model = EquipoTorneo
        fields = ['id', 'equipo', 'equipo_nombre', 'torneo', 'torneo_nombre']