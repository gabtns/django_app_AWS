from django.shortcuts import render
from .models import categoria
# Create your views here.

def categorias(request):
    categ_ = categoria.objects.all()
    return render(request,{"categ":categ_})