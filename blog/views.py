from django.shortcuts import render

def listar_publicacion(request):
    return render(request,'blog/listar_publicacion.html',{})
