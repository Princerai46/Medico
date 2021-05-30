from django.urls import path
from .views import hospitals

urlpatterns=[
    path('',hospitals)
    ]