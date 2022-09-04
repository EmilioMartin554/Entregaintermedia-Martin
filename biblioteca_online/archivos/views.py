from .models import libro, revista, texto
from django.shortcuts import render
from django.http import HttpResponse

def buscar(request):
    if request.method == "POST":
        titulo = request.POST["titulo"]
        if libro.objects.filter(titulo__contains=titulo):
            libros = libro.objects.filter(titulo__contains=titulo)
            return render(request,"buscar.html",{"libros":libros})
        elif revista.objects.filter(titulo__contains=titulo):
            revistas = revista.objects.filter(titulo__contains=titulo)
            return render(request,"buscar.html",{"revistas":revistas})
        elif texto.objects.filter(titulo__contains=titulo):
            textos = texto.objects.filter(titulo__contains=titulo)
            return render(request,"buscar.html",{"textos":textos})
        else:    
            return HttpResponse("material no encontrado")
    return render(request,"buscar.html")

def insertar_libros(request):
    if request.method == "POST":
        tomo = libro(fecha_de_publicacion = request.POST["fecha_de_publicacion"],autor = request.POST["autor"],titulo=request.POST["titulo"],link=request.POST["link"])
        tomo.save()
        return render(request,"insertar_libro.html")
    return render(request,"insertar_libro.html")

def insertar_revista(request):
    if request.method == "POST":
        tomo = revista(fecha_de_publicacion = request.POST["fecha_de_publicacion"],autor = request.POST["autor"],titulo=request.POST["titulo"],link=request.POST["link"])
        tomo.save()
        return render(request,"insertar_revista.html")
    return render(request,"insertar_revista.html")

def insertar_texto(request):
    if request.method == "POST":
        tomo = texto(fecha_de_publicacion = request.POST["fecha_de_publicacion"],autor = request.POST["autor"],titulo=request.POST["titulo"],link=request.POST["link"])
        tomo.save()
        return render(request,"insertar_texto.html")
    return render(request,"insertar_texto.html")
# Create your views here.
