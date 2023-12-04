from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics

from .serializers import FarmSerializer, ProduceSerializer, FarmPostSerializer, ProducePostSerializer
from .models import Farm, Produce
from users.models import Profile



@api_view(['GET'])
def getFarms(request):
    FarmSerializer(data=request.data, context={'request': request})
    qs = Farm.objects.all()
    serializer = FarmSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduces(request):
    ProduceSerializer(data=request.data, context={'request': request})
    qs = Produce.objects.all()
    serializer = ProduceSerializer(qs, many=True)
    return Response(serializer.data)


class SingleFarm(generics.ListAPIView):
    serializer_class = FarmSerializer

    def get_queryset(self):
        post_name = self.request.query_params.get('id', None)
        print(post_name)
        return Farm.objects.filter(id=id)
    

class SingleProduce(generics.ListAPIView):
    serializer_class = ProduceSerializer

    def get_queryset(self):
        post_name = self.request.query_params.get('id', None)
        print(post_name)
        return Produce.objects.filter(id=id)
    

@api_view(['POST'])
def addFarm(request):
    serializer = FarmPostSerializer(data=request.data)
    id = request.data['post_author']

    author = Profile.objects.filter(id=id)
    print(author[0].email)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['POST'])
def addProduce(request):
    serializer = ProducePostSerializer(data=request.data)
    id = request.data['post_author']

    author = Profile.objects.filter(id=id)
    print(author[0].email)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)