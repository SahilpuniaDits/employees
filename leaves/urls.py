from django.urls import path, include
from .views import *
urlpatterns = [
    
    path('login/', login , name = 'login'),
    path('signup/', signup, name= 'signup'),
    path('api/register', UserRegistrationView.as_view(), name='register'),
    path('api/login/', UserLoginView.as_view(), name='login1'),
    
]
