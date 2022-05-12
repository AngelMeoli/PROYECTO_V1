from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.http import HttpResponse
#from .capturandoRostros import registro_rostro

from django.http import HttpResponseRedirect


# Create your views here.

#def biometrico(request):
    
 #   registro_rostro()
  #  print("hola hola")
   # return HttpResponse( """" <html><script>window.location.replace('/');</script></html>""")


def registro(request):
    #form=UserCreationForm()
    if request.method == 'POST':
        
        form = CreateUserForm(request.POST)
        if form.is_valid():
            
            form.save()
            #registro_rostro()
            #    user = form.save()
            #    group = Group.objects.get(name='Customers')
           # user.groups.add(group)
            return render(request,'user/login.html')
            # ser-login
    else:
        form = CreateUserForm()
   
    return render(request, 'user/registro.html',{'form':form})





