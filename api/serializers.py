from rest_framework.serializers import ModelSerializer
from .models import Farm, Produce


class FarmSerializer(ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'
        depth = 1

class FarmPostSerializer(ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'


class ProduceSerializer(ModelSerializer):
    class Meta:
        model = Produce
        fields = '__all__'
        depth = 1

class ProducePostSerializer(ModelSerializer):
    class Meta:
        model = Produce
        fields = '__all__'