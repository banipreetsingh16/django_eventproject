from django.shortcuts import render
from rest_framework import  views
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate,login,logout
from rest_framework.response import Response
from rest_framework.views import APIView

from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail
from events.models import Participants
from .serializers import *
# Create your views here.

class CreateNewUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {"message":"User Registered Successfully"}
        return response
    
class ListUser(ListAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer

class LoginUser(views.APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username,password=password)
        login(request, user)
        u = User.objects.get(username = username)
        token = Token.objects.create(user = u)
        serializer = Userserializer(user)
        return Response({"data":serializer.data, "Token":token.key,})
    
class LogoutUser(views.APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        logout(request)
        return Response({"data":"Logout Successful"})
    

class PassNew(views.APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = User.objects.get(username=request.user)
        user.set_password(request.data['password'])
        user.save()
        return Response({"data":"Password Changed Successfully"})
    


# class SendFormEmail(View):

#     def  get(self, request):

#         # Get the form data 
#         name = request.GET.get('name', None)
#         email = request.GET.get('email', None)
#         message = request.GET.get('message', None)

#         # Send Email
#         send_mail(
#             'Subject - Django Email Testing', 
#             'Hello ' + name + ',\n' + message, 
#             'banipreet.singh@netsolutions.com', # Admin
#             [
#                 email,
#             ]
#         ) 

#         # Redirect to same page after form submit
#         messages.success(request, ('Email sent successfully.'))
#         return redirect('home') 

class Profile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.get(id = request.user.id)
        
        event_data = Participants.objects.filter(user=user)
        events = []
        for i in event_data:
            name=i.event_name.event_name
            
            print("===========================>")
            print(name)
            events.append(name)
        data = {
            "user":user.username,
            "Email":user.email,
            "events":events
        }
        return Response(data)
    