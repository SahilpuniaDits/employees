from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

from rest_framework import status
from rest_framework import serializers
from rest_framework import response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.permissions import IsAuthenticated
# from django.core.mail import EmailMultiAlternatives
# import random
from django.http import HttpResponse
# from rest_framework.decorators import list_route

from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    
   
)
# from utils import res_codes
import jwt
from .models import User

class UserRegistrationView(APIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny, )

    def post(self, request):        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()  
            
            status_code = status.HTTP_201_CREATED
            

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
                'user': serializer.data
            }

            return Response(response, status=status_code)
class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    # 'role': serializer.data['role']
                }
            }

            return Response(response, status=status_code)

