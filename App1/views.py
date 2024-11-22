from django.shortcuts import render,get_object_or_404,redirect
from .models import AutorModel,FraseModel
from .forms import CreatenewAutor

# Create your views here.
def IndexView(request):
    objeto=AutorModel.objects.all().order_by("id")
    return render(request,"index.html",{"autores":objeto})

def AutorView(request,id):
    autor=get_object_or_404(AutorModel,pk=id)
    return render(request,"autor.html",{"autor":autor})

def create_autorView(request):
    if request.method=="GET":
        return render(request,"create_autores.html",{"form":CreatenewAutor})
    else:
        AutorModel.objects.create(nombre=request.POST["nombre"],fecha_nacimiento=request.POST["fecha_nacimiento"],fecha_fallecimiento=request.POST["fecha_fallecimiento"],nacionalidad=request.POST["nacionalidad"])
        return redirect(request.path)
