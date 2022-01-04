from django.urls import path, include
from .views import *
urlpatterns = [
    
    path('login/', login , name = 'login'),
    path('signup/', signup, name= 'signup'),
    path('deshboard/', deshboard , name = 'deshboard'),
    path('leaves/', leaves, name= 'leaves'),

    path('api/register', UserRegistrationView.as_view(), name='register'),
    path('api/login/', UserLoginView.as_view(), name='login1'),
    path('api/leaves/', applyleaves.as_view(), name='leave'),

    
]