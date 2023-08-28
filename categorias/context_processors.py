from .models import categoria

def menu_links(request):
    links = categoria.objects.all()
    print(links)
    return dict(link = links)