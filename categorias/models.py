from django.db import models
from django.urls import reverse

# Create your models here.
class categoria(models.Model):
    name_category = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=100,blank=True)
    slug = models.CharField(max_length=100,unique=True)
    cat_image = models.ImageField(upload_to='categoria')
    created = models.DateTimeField(auto_now_add=True,verbose_name='creado')
    update = models.DateTimeField(auto_now=True,verbose_name='cambio')
    

    class Meta:
        verbose_name = 'nombre categoria'
        verbose_name_plural = 'nombres de categorias'

    def get_url(self):
        return reverse('product_by_categories',args = [self.slug])

    def __str__(self) -> str:
        return self.name_category