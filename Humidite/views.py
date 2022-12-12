from django.shortcuts import render
from rest_framework import viewsets
from Humidite.serializer import HumideSerializer
from Humidite.models import Plante

# Creation de la classe HumiditeViewSet qui heritera de la classe ModelViewSet
class HumiditeViewSet(viewsets.ModelViewSet):
    #   Point de terminaison de l'API qui permet de visualiser
    queryset = Plante.objects.all() # on indique les donnees 
    serializer_class = HumideSerializer
    
# Il faut definir les urls qui permettront d'acceder aux endpoints de nos API

def accueil(request):
    return render(request, 'humidite/accueil.html')

def humidite(request):
    return render(request, 'humidite/humide.html')
