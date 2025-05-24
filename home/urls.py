from django.urls import path 

from home import views

urlpatterns = [
    
    path('', views.HomeView.as_view(), name='home'),
   # path('authorized', views.AuthorizedView.as_view()),
    path('login',  views.LoginInterfaceView.as_view(), name='login'),
    #path('logout', views.LogoutInterfaceView.as_view(),  name='logout'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupInterfaceView.as_view(), name='signup'),  


    
]