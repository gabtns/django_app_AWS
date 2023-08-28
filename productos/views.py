from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import productos
from categorias.models import categoria
# Create your views here.


def store(request,categoria_slug = None):
    product = None
    categories = None
    if categoria_slug != None:
        cat = get_object_or_404(categoria, slug = categoria_slug)
        elementos = productos.objects.all().filter(categoria = cat ,is_available = True)
        contar = elementos.count()
    else:
        elementos = productos.objects.all().filter(is_available = True)
        cat = categoria.objects.all()
        contar = elementos.count()

    contexto = {
        "elementos":elementos ,
        "categoria":cat,
        "contar":contar}

    return render(request,"productos/store.html",contexto)
  

def product_detail(request,  categoria_slug,product_slug ):
    ''' try:
        single = productos.objects.get(categoria__slug = categoria_slug,slug = product_slug )
        #Obtengo el producto, comparo si la categoria que tengo es igual a la categoria que entra por parametro. 
        #Luego la condicion de la categoria correspondiente sera comparado con la categoria del producto.
    except Exception as e:
        print("error")
    
    producto = {
        "single": single,
    }''' 
    
    return render(request,"productos/product-detail.html")
