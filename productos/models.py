from django.db import models
from django.urls import reverse
from categorias.models import categoria
# Create your models here.
class productos(models.Model):
    name = models.CharField(max_length= 100,verbose_name= "nombre",unique=True)
    description = models.CharField(max_length= 100,verbose_name= "descripcion")
    marca = models.CharField(max_length= 100,verbose_name= "marca")
    slug = models.CharField(max_length=200)
    images = models.ImageField(upload_to='productos',verbose_name= "images")
    precio = models.IntegerField(max_length=10,verbose_name="precio")
    stock = models.IntegerField(max_length=10,verbose_name="stock")
    is_available = models.BooleanField(default=True)
    categoria = models.ForeignKey(categoria, on_delete = models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    cambio = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'nombre'
        verbose_name_plural = "nombres"

    def get_url(self):
        return reverse('product-detail',args = [self.categoria.slug,self.slug])    

    def __str__(self) -> str:
        return self.name