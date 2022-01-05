from django.urls import path, include
from .views import *
urlpatterns = [
    
    path('login/', login , name = 'login'),
    path('signup/', signup, name= 'signup'),
    path('deshboard/', deshboard , name = 'deshboard'),
    path('leaves/', leaves, name= 'leaves'),

    path('api/register', UserRegistrationView.as_view(), name='register'),
    path('api/login/', UserLoginView.as_view(), name='login1'),
    path('api/applyleaves/', applyleaves.as_view(), name='leave'),
    path('api/leavesget/', leavesget.as_view(), name='leavesget'),
    path('api/leavesget/<int:id>/', leavegetid.as_view(), name='leavegetid'),

    path('api/update/<int:id>/', leavesUpdate.as_view(), name='update'),
    path('api/delete/<int:id>/', leavesDelete.as_view(), name='delete'),


    
]