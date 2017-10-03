from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostearForm
from .models import publicar

def listar_publicacion(request):
    publi = publicar.objects.filter(fecha_publicacion__lte=timezone.now()).order_by ('fecha_publicacion')
    return render(request,'blog/listar_publicacion.html',{'publi':publi})

def detalle_publicacion(request,pk):
    p = get_object_or_404(publicar, pk=pk)
    return render(request,'blog/detalle_publicacion.html',{'p':p})

def nueva_publicacion(request):
    if request.method == "POST":
        f = PostearForm(request.POST)
        if f.is_valid():
            p = f.save(commit=False)
            p.autor = request.user
            # p.fecha_publicacion = timezone.now() para que no incluya fecha de publicacion siendo borrrador
            p.save()
            return redirect('postear', pk=p.pk)
    else:
        f = PostearForm()
    return render(request, 'blog/nueva_publicacion.html', {'f': f})

def editar_publicacion(request,pk):
    p = get_object_or_404(publicar, pk=pk)
    if request.method == "POST":
        f = PostearForm(request.POST, instance=p)
        if f.is_valid():
            p = f.save(commit=False)
            p.autor = request.user
            # p.fecha_publicacion = timezone.now() para que no incluya fecha de publicacion siendo borrrador
            p.save()
        return redirect('postear', pk=p.pk)
    else:
        f = PostearForm(instance=p)
    return render(request, 'blog/nueva_publicacion.html', {'f': f})

def borradores_publicacion(request):
        f = publicar.objects.filter(fecha_publicacion__isnull=True).order_by('fecha_creacion')
        return render(request,'blog/borradores_publicacion.html',{'f':f})

def postear_publicacion(request, pk):
        p = get_object_or_404(publicar, pk=pk)
        p.publish()
        return redirect('postear', pk=p.pk)
