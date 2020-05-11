from django.contrib import admin
from django.urls import path,include
from .views import (
ExposeListView,
ExposeDeleteView,
ExposeDetailView,
ExposeUpdateView,
ExposeCreateView,
)

urlpatterns = [

    path('', ExposeListView.as_view(), name="expose_list"),
    path('new/', ExposeCreateView.as_view(), name="expose_new"),
    path('<int:pk>', ExposeDetailView.as_view(), name="expose_detail"),
    path('<int:pk>/edit', ExposeUpdateView.as_view(), name="expose_edit"),
    path('<int:pk>/delete', ExposeDeleteView.as_view(), name="expose_delete"),

]


