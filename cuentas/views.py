from django.shortcuts import render
from .models import Myaccount
# Create your views here.
def cuentas(request):
    cuenta = Myaccount.objects.all()
    render(request,{"cuentas":cuenta})