from rest_framework import serializers
from Humidite.models import Plante


# Les sérialiseurs définissent la représentation de l'API.
# Creation de  classe serializer pour faire la conversion entre model et json
# ici la classe ModelSerializer permet de mapper un model en json
class HumideSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Plante # ca prend le model a mapper
        fields = '__all__' # tous les donnes du models comvernees

# Par la suite il faut creer les vues qui vont recevoir les differents call API et 
# qui vont les traiter en utilisants les serializer creer en haut