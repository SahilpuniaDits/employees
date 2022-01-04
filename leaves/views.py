from rest_framework import status
from .models import User
import jwt
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,


)
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from rest_framework import response
from rest_framework import serializers
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def deshboard(request):
    return render(request, 'index.html')
def leaves(request):
    return render(request, 'leaves.html')

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
# from rest_framework.decorators import list_route


from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    leaveSerializer
    
   
)
# from utils import res_codes
import jwt
from .models import User,leave

# from utils import res_codes


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
                # 'authenticatedUser': {
                #     'email': serializer.data['email'],
                #     'role': serializer.data['role']
                # }
            }
            return Response(response)
            # print('--09-9-09-0909', response)

class applyleaves(APIView):
    serializer_class = leaveSerializer
    permission_class = (AllowAny, )
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success':True,
                'status':status_code,
                'massage':'your leaves is apply successfully',
                'user':serializer.data
            }
            return Response(response)
        else:
            response = {
                'success':False,
                'massage':'please enter correct input',
                'user':serializer.data
            }
            return Response(response,status = status.HTTP_400_BAD_REQUEST)


