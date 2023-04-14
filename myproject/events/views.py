from django.shortcuts import render
from django.shortcuts import render
from rest_framework import  viewsets, filters, views
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Events, Participants
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate,login,logout
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from rest_framework.views import APIView


# Create your views here.

class EventSerializer(ModelSerializer):
    class Meta:
        model=Events
        fields='__all__'

class RegisterEvent(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        response =  super().create(request, *args, **kwargs)
        response.data = {"message":"Event Created Successfully"}
        return response
    
class EventJoin(APIView):
    permission_classes = [IsAuthenticated]
   
    def post(self, request, pk):
        eve = Events.objects.get(id = pk)
        request.data['user'] = request.user.id
        Participants.objects.create(user = request.user, event_name = eve)
        return Response({"data":"Congratulations you have successfully joined the event!!!!"})
    
class FilterEvent(FilterSet):
    event_name = CharFilter(lookup_expr='contains')
    class Meta:
        model = Events
        fields = ['event_name']

class EventSearch(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FilterEvent

