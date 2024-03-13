from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def home(request):
  return render(request, "aplicacion/index.html")

def remeras(request):
  contexto = {'remeras': Remera.objects.all()}
  return render(request, "aplicacion/remeras.html")

def pantalones(request):
  contexto = {'pantalones': Pantalon.objects.all()}
  return render(request, "aplicacion/pantalones.html")

def buzos(request):
  contexto = {'buzos': Buzo.objects.all()}
  return render(request, "aplicacion/buzos.html")

def clientes(request):
  contexto = {'clientes' : Cliente.objects.all()}
  return render(request, "aplicacion/clientes.html")

def vendedores(request):
  contexto = {'vendedores' : Vendedor.objects.all()}
  return render(request, "aplicacion/vendedores.html")


def acerca(request):
  return render(request, "aplicacion/acerca.html")

def agregar_cliente(request):
  cliente = Cliente(nombre = "Joaco", apellido = "Gonzalez")
  cliente.save()
  respuesta = f"<html><h1>Se guardo el cliente</h1> </html>"
  return HttpResponse(respuesta)

def agregar_vendedor(request):
  vendedor = Vendedor(nombre = "Empresario")
  vendedor.save()
  respuesta = f"<html><h1>Se guardo el vendedor</h1> </html>"
  return HttpResponse(respuesta)


def agregar_remera(request):
  remera = Remera(articulo = "articulo", categoria = "categoria", modelo = "modelo", talle = "talle")
  remera.save()
  respuesta = f"<html><h1>Se guardo el articulo</h1> </html>"
  return HttpResponse(respuesta)

#______________forms

def clienteForm(request):
  if request.method == "POST":
    miForm = ClienteForm(request.POST)
    if miForm.is_valid():
      cliente_nombre = miForm.cleaned_data.get("nombre")
      cliente_apellido = miForm.cleaned_data.get("apellido")
      cliente = Cliente(nombre = cliente_nombre, apellido = cliente_apellido)
      cliente.save()
      return render(request, "aplicacion/index.html")
  else:
    miForm = ClienteForm()
    
  return render(request, "aplicacion/clienteForm.html", {"form": miForm})


def remeraForm(request):
  if request.method == "POST":
    miForm = RemeraForm(request.POST)
    if miForm.is_valid():
      remera_nombre = miForm.cleaned_data.get("articulo")
      remera_categoria = miForm.cleaned_data.get("categoria")
      remera_modelo = miForm.cleaned_data.get("modelo")
      remera_talle = miForm.cleaned_data.get("talle")
      remera = Remera(articulo = remera_nombre,  categoria = remera_categoria, modelo = remera_modelo, talle = remera_talle)
      remera.save()
      return render(request, "aplicacion/index.html")
  else:
    miForm = RemeraForm()
    
  return render(request, "aplicacion/remeraForm.html", {"form": miForm})

def pantalonForm(request):
  if request.method == "POST":
    miForm = PantalonForm(request.POST)
    if miForm.is_valid():
      pantalon_nombre = miForm.cleaned_data.get("articulo")
      pantalon_categoria = miForm.cleaned_data.get("categoria")
      pantalon_modelo = miForm.cleaned_data.get("modelo")
      pantalon_talle = miForm.cleaned_data.get("talle")
      pantalon = Pantalon(articulo = pantalon_nombre,  categoria = pantalon_categoria, modelo = pantalon_modelo, talle = pantalon_talle)
      pantalon.save()
      return render(request, "aplicacion/index.html")
  else:
    miForm = PantalonForm()
    
  return render(request, "aplicacion/pantalonForm.html", {"form": miForm})

def buzoForm(request):
  if request.method == "POST":
    miForm = BuzoForm(request.POST)
    if miForm.is_valid():
      buzo_nombre = miForm.cleaned_data.get("articulo")
      buzo_categoria = miForm.cleaned_data.get("categoria")
      buzo_descripcion = miForm.cleaned_data.get("descripcion")
      buzo_talle = miForm.cleaned_data.get("talle")
      buzo = Buzo(articulo = buzo_nombre,  categoria = buzo_categoria, descripcion = buzo_descripcion, talle = buzo_talle)
      buzo.save()
      return render(request, "aplicacion/index.html")
  else:
    miForm = BuzoForm()
    
  return render(request, "aplicacion/buzoForm.html", {"form": miForm})



def buscar(request):
  return render(request, "aplicacion/buscar.html")


def encontrarArticulo(request):
  if request.GET["buscar"]:
    patron = request.GET["buscar"]
    remera = Remera.objects.filter(articulo__icontains = patron)
    contexto = {"remeras": remera}
    return render(request, "aplicacion/remeras.html", contexto)
  
  contexto = {"remeras": Remera.objects.all()}
  return render(request, "aplicacion/buscar.html")