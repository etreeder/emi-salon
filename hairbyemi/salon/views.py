from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

from .models import Image, Service

# Create your views here.
class Index(TemplateView):
    template_name = 'salon/index.html'

# GALLERY VIEWS
class Gallery(ListView):
    template_name = 'salon/gallery.html'
    model=Image
    
class ImageCreate(CreateView):
    model = Image
    fields = '__all__'
    template_name = 'salon/image.html'
    success_url = '/gallery'
    
    
# SERVICE VIEWS
class Services(ListView):
    template_name = 'salon/service/services.html'
    model=Service
    
class ServiceDetail(DetailView):
    model = Service
    template_name = 'salon/service/service-detail.html'
    context_object_name = 'service'
    
class ServiceCreate(CreateView):
    model=Service
    fields="__all__"
    success_url = "/services"
    template_name = 'salon/service/service-create.html'
    
class ServiceUpdate(UpdateView):
    model=Service
    fields="__all__"
    success_url = "/services"
    template_name = 'salon/service/service-update.html'
    
class ServiceDelete(DeleteView):
    model=Service
    success_url = "/services"
    template_name = 'salon/service/service-delete.html'

    
