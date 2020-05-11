from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DeleteView,DetailView,UpdateView,CreateView
from django.urls import reverse_lazy
from .models import Expose

class ExposeListView(ListView):
    model = Expose
    template_name = "expose_list.html"

class ExposeDetailView(DetailView):
    model = Expose
    template_name = "expose_detail.html"

class ExposeUpdateView(UpdateView):
    model = Expose
    fields = ("title","pdf","description")
    template_name = "expose_edit.html"

class ExposeDeleteView(DeleteView):
    model = Expose
    template_name = "expose_delete.html"
    success_url = reverse_lazy("expose_list")

class ExposeCreateView(CreateView):
    model = Expose
    template_name = "expose_new.html"
    fields = ("title","pdf","description","author")
