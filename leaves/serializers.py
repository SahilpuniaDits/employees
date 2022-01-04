
<<<<<<< HEAD
from django.db.models import fields
from .models import User,leave
=======

# class registerSerializer(serializers.ModelSerializer):
#     username=serializers.CharField(max_length=100)
#     email=serializers.EmailField(max_length=255,min_length=4)
#     password=serializers.CharField(max_length=100)
#     first_name=serializers.CharField(max_length=100)
#     last_name=serializers.CharField(max_length=100)

#     class Meta:
#         model=User
#         fields='__all__'

#     def save(self):
#         email=self.validated_data['email']
#         username=self.validated_data['username']
#         if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
#             raise serializers.ValidationError({'account':'account is already exists'})
#         else:
#             user=User.objects.create(
#             username=self.validated_data['username'],
#             first_name=self.validated_data['first_name'],
#             last_name=self.validated_data['last_name'],
#             email=self.validated_data['email'],
#             )
#             password=self.validated_data['password']
#             user.is_active=True
#             user.set_password(password)
#             user.save()
#             return user
# class loginSerializer(serializers.ModelSerializer):
#     username=serializers.CharField(max_length=100)
#     password=serializers.CharField(max_length=100)

#     class Meta:
#         model=User
#         fields='__all__'
#     def save(self):
#         username=self.validated_data['username']
#         password=self.validated_data['password']
#         if username and password:
#             user=authenticate(username=username,password=password)
#             if user:
#                 if user.is_active:
#                     return user
#                 else:
#                     raise serializers.ValidationError({'user':'user is not active'})
#             else:
#                 raise serializers.ValidationError({'user':'please enter valid user credentails'})
#         else:
#             raise serializers.ValidationError({'error':'username and password not to be blank'})

# class resetpasswordSerializer(serializers.ModelSerializer):
#     username=serializers.CharField(max_length=100)
#     password=serializers.CharField(max_length=100)

#     class Meta:
#         model=User
#         fields='__all__'
#     def save(self):
#         username=self.validated_data['username']
#         password=self.validated_data['password']
#         #filtering out whethere username is existing or not, if your username is existing then if condition will allow your username
#         if User.objects.filter(username=username).exists():
#         #if your username is existing get the query of your specific username
#             user=User.objects.get(username=username)
#             #then set the new password for your username
#             user.set_password(password)
#             user.save()
#             return user
#         else:
#             raise serializers.ValidationError({'error':'please enter valid crendentials'})


from .models import User
>>>>>>> 41abf34edadf650ce0e6db63ce8d52d13ccef08c
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, Token
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import check_password
# from utils import res_codes

import jwt
from rest_framework.permissions import IsAuthenticated


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'password'
        )

    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    # role = serializers.CharField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        email = data['email']
        password = data['password']
        print('-----======', password)
        print('---====', email)
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            # update_last_login(None, user)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email,
                # 'role': user.role,
            }

            print('---00000', validation)

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")
<<<<<<< HEAD


class leaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = leave
        fields = ("__all__")
=======
>>>>>>> 41abf34edadf650ce0e6db63ce8d52d13ccef08c
