from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    entrenador = models.CharField(max_length=50)
    escudo = models.ImageField(upload_to='escudo_equipos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Torneo(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class EquipoTorneo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.equipo.nombre} en {self.torneo.nombre}"

class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    posicion = models.CharField(max_length=20)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='jugador_foto/', blank=True, null= True)

    def __str__(self):
        return self.nombre
    
class Partido(models.Model):
    fecha = models.DateField()
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_como_local')
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_como_visitante')
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, related_name='partidos_del_torneo')
    goles_local = models.IntegerField()
    goles_visitante = models.IntegerField()

    def __str__(self):
        return f"{self.equipo_local.nombre} vs {self.equipo_visitante.nombre} ({self.torneo.nombre} - {self.fecha})"
