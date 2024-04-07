from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'home.html')

def singup(request):
    
    if request.method == 'GET':
        print('enviando datos')
        return render(request, 'singup.html', {
        'form' : UserCreationForm
    })

    
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #Registrando User
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect('task')
            except:
                return render(request, 'singup.html', {
                        'form' : UserCreationForm,
                        "error" : 'Usuario ya existente'})
        
        return render(request, 'singup.html', {
                        'form' : UserCreationForm,
                        "error" : 'Contraseñas no son iguales'
            })

def task (request):
    return render(request, 'task.html')  
    
