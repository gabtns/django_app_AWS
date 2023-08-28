from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("",views.store,name="store"),
    path("<slug:categoria_slug>/" ,views.store,name="product_by_categories"),
    path("<slug:categoria_slug>/<slug:product_slug>/" ,views.product_detail,name= 'product_detail'),
]