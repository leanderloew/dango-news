from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from .views import SignUpView


urlpatterns = [
    path('signup/',SignUpView.as_view(), name="signup") #this will be tackled first
]
