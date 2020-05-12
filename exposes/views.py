from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DeleteView,DetailView,UpdateView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Expose

class ExposeListView(LoginRequiredMixin,ListView):
    model = Expose
    template_name = "expose_list.html"

class ExposeDetailView(LoginRequiredMixin,DetailView):
    model = Expose
    template_name = "expose_detail.html"

class ExposeUpdateView(LoginRequiredMixin,UpdateView):
    model = Expose
    fields = ("title","pdf","description")
    template_name = "expose_edit.html"

class ExposeDeleteView(LoginRequiredMixin,DeleteView):
    model = Expose
    template_name = "expose_delete.html"
    success_url = reverse_lazy("expose_list")

class ExposeCreateView(LoginRequiredMixin,CreateView):
    model = Expose
    template_name = "expose_new.html"
    fields = ("title","pdf","description")

    def form_valid(self, form):
        #request reflects the incomming data
        form.instance.author=self.request.user
        return super().form_valid(form)
