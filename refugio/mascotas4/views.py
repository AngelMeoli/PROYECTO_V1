from re import template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import usuario_solicitud_form, mascota_form
from .models import usuario_solicitud, Mascota
from django.contrib.auth.decorators import login_required


# Create your views here.

def ejemplo(request):
    return render(request, 'barra.html') 


def ingreso_solicitud(request):
    if request.method=='POST':
        form=usuario_solicitud_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascotas4:mascota_listar')

    else:
        form=usuario_solicitud_form()

    return render(request,'solicitud/registro_solicitud.html',{'form':form})

@login_required(login_url='user-login')
def listar_solicitudes(request):
    solicitud=usuario_solicitud.objects.all()
    contexto={'solicitudes':solicitud}
    return render(request, "solicitud/listar_solicitudes.html",contexto)

@login_required(login_url='user-login')
def solicitud_edit(request, id):  
    solicitud = usuario_solicitud.objects.get(id=id)
    if request.method == 'GET':
        form = usuario_solicitud_form(instance=solicitud)       
    else:       
        form = usuario_solicitud_form(request.POST, instance=solicitud)
        if form.is_valid():
            form.save()
        return redirect('mascotas4:solicitud_listar')
    return render(request,'solicitud/registro_solicitud.html',{'form':form})
@login_required(login_url='user-login')
def solicitud_delete(request,id):
    solicitud = usuario_solicitud.objects.get(id=id)
    if request.method == 'POST':
        solicitud.delete()
        return redirect('mascotas4:solicitud_listar')
    return render(request,'solicitud/solicitud_delete.html',{'solicitud':solicitud})

##########################################################################
@login_required(login_url='user-login')
def ingreso_mascota(request):
    if request.method=='POST':
        form=mascota_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascotas4:mascota_listar')

    else:
        form=mascota_form()

    return render(request,'mascotas/registro_mascota.html',{'form':form})


def listar_mascotas(request):
    mascota=Mascota.objects.all()
    contexto={'mascotas':mascota}
    return render(request, "mascotas/ver_mascotas.html",contexto)

@login_required(login_url='user-login')
def mascota_edit(request, id):  
    mascota = Mascota.objects.get(id=id)
    if request.method == 'GET':
        form = mascota_form(instance=mascota)       
    else:       
        form = mascota_form(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascotas4:mascota_listar')
    return render(request,'mascotas/registro_mascota.html',{'form':form})

@login_required(login_url='user-login')
def mascota_delete(request,id):
    mascota = Mascota.objects.get(id=id)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascotas4:mascota_listar')
    return render(request,'mascotas/mascota_delete.html',{'mascota':mascota})






"""
class Mascota_list(ListView):
    model=Mascota
    template_name='mascotas/ver_mascotas.html'
    
class MascotaCreate(CreateView):
    model=Mascota
    form_class= mascota_form
    template_name='mascotas/registro_mascota.html'
    success_ulr= reverse_lazy('mascotas4:mascota_listar')

"""


