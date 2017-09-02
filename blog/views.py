from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import publicar

def listar_publicacion(request):
    publi = publicar.objects.filter(fecha_publicacion__lte=timezone.now()).order_by ('fecha_publicacion')
    return render(request,'blog/listar_publicacion.html',{'publi':publi})

def detalle_publicacion(request,pk):
    p = get_object_or_404(publicar, pk=pk)
    return render(request,'blog/detalle_publicacion.html',{'p':p})
