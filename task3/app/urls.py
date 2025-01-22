from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('greet_or_redirect/', views.greet_or_redirect),
]