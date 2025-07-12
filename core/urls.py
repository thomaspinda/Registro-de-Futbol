from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.home, name='home'),
    # URLs para Equipos
    path('equipos/', views.lista_equipos, name='lista_equipos'),
    path('equipos/crear/', views.crear_equipo, name='crear_equipo'),
    path('equipos/editar/<int:pk>/', views.editar_equipo, name='editar_equipo'),
    path('equipos/eliminar/<int:pk>/', views.eliminar_equipo, name='eliminar_equipo'),

    # URLs para Jugadores
    path('jugadores/', views.lista_jugadores, name='lista_jugadores'),
    path('jugadores/crear/', views.crear_jugador, name='crear_jugador'),
    path('jugadores/editar/<int:pk>/', views.editar_jugador, name='editar_jugador'),
    path('jugadores/eliminar/<int:pk>/', views.eliminar_jugador, name='eliminar_jugador'),
]


router = DefaultRouter()

router.register(r'paises', views.PaisViewSet)
router.register(r'equipos', views.EquipoAPIViewSet)
router.register(r'torneos', views.TorneoViewSet)
router.register(r'equipos_torneo', views.EquipoTorneoViewSet)
router.register(r'jugadores', views.JugadorAPIViewSet)
router.register(r'partidos', views.PartidoViewSet)

urlpatterns += [
    path('api/', include(router.urls)),
]