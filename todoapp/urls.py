from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.log_out, name='logout'),
    path('home/', views.create, name='home'),  
    path('finished/<int:pk>/', views.finished, name='finished'),  
    path('delete/<int:pk>/', views.delete, name='delete'), 
]
