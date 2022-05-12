

# Create your views here.



from re import template
import re
from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import usuario_solicitud_form, mascota_form
from .models import usuario_solicitud, Mascota2
from django.contrib.auth.decorators import login_required


# Create your views here.
def formulario_adopcion(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = usuario_solicitud_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            otr=form.cleaned_data
            #Insertando en la base de datos
            nuevo=usuario_solicitud(
                cui=otr['cui']
                ,edad=otr['edad']
                ,telefono=otr['telefono']
                ,domicilio=otr['domicilio']
                ,numero_mascotas=otr['numero_mascotas']
                ,motivo_solicitud=otr['motivo_solicitud']                
                )
            nuevo.save()

            return render(request,'mascotas/ver_mascotas.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = usuario_solicitud_form()

    return render(request, 'mascotas/solicitud_adp.html', {'form': form})

def ejemplo(request):
    return render(request, 'barra.html') 



def ver_mascotas(request):
    mascota=Mascota2.objects.all()
    contexto={'mascotas':mascota}
    return render(request, "mascotas/ver_mascotas.html",contexto)


def mascota_edit(request, id):
  
    mascota = Mascota2.objects.get(id_mascota=id)
    print(mascota)
    if request.method == 'GET':
        form = mascota_form(instance=mascota)
        
    else:
        
        form = mascota_form(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascotas3:mascota_listar')
    return render(request,'mascotas/registro_mascota.html',{'form':form})


def ingreso_mascota(request):
    if request.method=='POST':
        form=mascota_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascotas3:mascota_listar')

    else:
        form=mascota_form()

    return render(request,'mascotas/registro_mascota.html',{'form':form})




class Mascota_list(ListView):
    model=Mascota2
    template_name='mascotas/ver_mascotas.html'
    


class MascotaCreate(CreateView):
    model=Mascota2
    form_class= mascota_form
    template_name='mascotas/registro_mascota.html'
    success_ulr= reverse_lazy('mascotas3:mascota_listar')





