"""from pydoc import doc
from django.template import Template, Context, loader
from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

@login_required(login_url='user-login')
def inicio(request):  #primera vista

    #doc_externo=open("C:/Users/angel/Desktop/PROYECTOS/mascotas/app/app/Plantillas/miplantilla.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    
    #doc_externo=loader.get_template('index.html')
    #ctx=Context()
    #Documento=doc_externo.render()  #le puedo pasar un diccionario directamente en esta linea

    return render(request,"inicio.html")

@login_required(login_url='user-login')
def registro_mascota(request):
    return render(request, "registro_mascota.html")

#@login_required(login_url='user-login')
def solicitud_adp(request):
    return render(request, "solicitud_adp.html")


@login_required(login_url='user-login')
def registro_usuario(request):
    return render(request, "registro_usuario.html")



"""