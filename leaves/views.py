from .models import User, leave
from rest_framework import status
from .models import User
import jwt
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    leaveSerializer,


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


# from django.core.mail import EmailMultiAlternatives
# import random
# from rest_framework.decorators import list_route


# from utils import res_codes

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
        print('hyere ---here---here---here',
              self.serializer_class(data=request.data))
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        print('hyere ---', serializer)

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

            print('--09-9-09-0909', response)
            return Response(response)


class applyleaves(APIView):
    serializer_class = leaveSerializer
    permission_class = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'status': status_code,
                'massage': 'your leaves is apply successfully',
                'user': serializer.data
            }
            return Response(response)
        else:
            response = {
                'success': False,
                'massage': 'please enter correct input',
                'user': serializer.data
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

            # return Response(response,status = status.HTTP_400_BAD_REQUEST)

class leavesget(APIView):
    def get(self,request):
        dataleave = leave.objects.all()
        serializer = leaveSerializer(dataleave,many = True)
        return Response(serializer.data)

class leavegetid(APIView):
    def get_object(self,id):
        return leave.objects.get(id=id)
    def get(self,request,id):
        getid = self.get_object(id=id)
        serializer = leaveSerializer(getid)
        return Response(serializer.data)



class leavesUpdate(APIView):
    def get_object(self,id):
        return leave.objects.get(id=id)
    def put(self,request,id):
        leave = self.get_object(id)
        serializer = leaveSerializer(leave,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class leavesDelete(APIView):
    def get_object(self,id):
        return leave.objects.get(id=id)
    def delete(self,request,id):
        leavedelete = self.get_object(id)
        leavedelete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




