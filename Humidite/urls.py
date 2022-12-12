from rest_framework import routers
from Humidite.views import HumiditeViewSet, TouchViewSet

router = routers.DefaultRouter()
router.register('humides', HumiditeViewSet) #Enregistre la route
router.register('touchs', TouchViewSet) #Enregistre la route


#Par la suite importer nos urls dans le url root se trouvant dans le meme dossier que settings.py