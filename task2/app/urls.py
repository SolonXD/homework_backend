from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('greet/', views.greet),
    path('greet_full/', views.greet_full),
    path('create/', views.create)
]