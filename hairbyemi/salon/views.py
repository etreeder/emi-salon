from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

from .models import Image

# Create your views here.
class Index(TemplateView):
    template_name = 'salon/index.html'

class Gallery(ListView):
    template_name = 'salon/gallery.html'
    model=Image
    
    
class Image(CreateView):
    model = Image
    fields = '__all__'
    template_name = 'salon/image.html'
    success_url = '/gallery'