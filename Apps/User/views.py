
from http.client import HTTPResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from Apps.User.models import User_profile
from Apps.User.forms import User_profile_Form, UserEditForm, User_registration_form,UserEditPerfilForm

########### USUARIO  ############################################################

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password= form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                context = f'Bienvenido {username} al portal'
                return render(request, 'User/Respuesta.html', {"context" : context})
            else:
                context = {'error': 'Usuario o contraseña incorreccto'}
                form = AuthenticationForm()
                return render (request, 'User/login.html', context=context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'error':'Error: Datos incorrecctos', 'form':form}
            return render (request, 'User/login.html', context=context)
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'User/login.html',context=context)


def register_view(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)

            context= {'message': f'Usuario {username} creado exitosamente'}
            return render(request, 'User/respuesta.html', {'context': f'Usuario {username} creado exitosamente'})
        else:
            errors = form.errors
            form = User_registration_form()
            context = {'errors':errors, 'form': form} 
            return render(request, 'User/register.html', context=context)
    else:
        form = User_registration_form()
        context = {'form': form}
        return render (request, 'User/register.html', context = context)


def logout_view(request):
    logout(request)
    return render(request, "User/respuesta.html",{"context":f"Cerraste sesión"})


@login_required
def edit_user(request,id):
    usuario=request.user
    if request.method == 'POST':
        miFormulario=UserEditForm(request.POST, instance=request.user)
        if miFormulario.is_valid():
           info= miFormulario.cleaned_data
           usuario.username=info["username"]
           usuario.email=info["email"]
           usuario.set_password(info["password1"])
        #    usuario.set_password(info["password2"])
           usuario.save()
                # return redirect('perfil')
        return render(request, 'User/respuesta.html', {'context': f'Usuario {usuario.username} creado exitosamente'})
    else:
        miFormulario= UserEditForm(instance=request.user)
        return render (request,'User/edit_usuario.html',{"miFormulario":miFormulario, "usuario":usuario})


@login_required
def del_user(request,id):
    profile = User.objects.get(id=id)
    if request.method == 'GET':
        mensaje = 'Esta por eliminar sus datos de usuario'
        form = User_registration_form(initial={
            "username": profile.username,
            "email": profile.email
        })
        context = {'form':form,'mensaje':mensaje}
        return render (request,'User/del_user.html',context)
    else:
        profile = User.objects.get(id=id)
        profile.delete()
        return redirect('index')


################ PERFIL ##################################################################

@login_required
def create_perfil(request):
    if request.method == "POST":
        form = User_profile_Form(request.POST, request.FILES)
        if form.is_valid():
            User_profile.objects.create(
                    user = request.user,
                    phone = form.cleaned_data['phone'],
                    first_name = form.cleaned_data['first_name'],
                    last_name = form.cleaned_data['last_name'],
                    direccion = form.cleaned_data['direccion'],
                    description= form.cleaned_data['description'],
                    image = form.cleaned_data['image']
                )   
            return redirect ("perfil")
        else:
            return render (request, "User/respuesta.html", {"context":f"los cambios no se han realizado"})
    else:
        miFormulario = User_profile_Form()
        return render (request, "User/crear_profile.html",{"miFormulario":miFormulario})


@login_required
def show_perfil (request):
    if request.user.is_authenticated:
        usuario = (
            request.user.profile.first_name,
            request.user.profile.last_name,
            request.user.profile.phone,
            request.user.profile.direccion,
            request.user.profile.description,
            request.user.profile.image 
        )
    return render(request, 'User/profile.html', {"usuario":usuario})


@login_required
def edit_perfil(request,id):
    profile = get_object_or_404(User_profile,user=request.user)
    if request.method == 'POST':
        form = User_profile_Form(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            profile.save()
            return redirect('perfil')
    else:
        form = User_profile_Form(instance=profile)
        context = {'form':form,'perfil':profile}
        return render (request,'User/edit_profile.html',context)


@login_required
def eliminar_perfil(request,id):
    profile = get_object_or_404(User_profile,user=request.user)
    if request.method == 'GET':
        mensaje = 'Esta por borrar sus datos de perfil'
        form = User_profile_Form(instance=profile)
        context = {'form':form,'mensaje':mensaje}
        return render (request,'User/del_profile.html',context)
        
    else:
        profile = User_profile.objects.get(id=id)
        profile.delete()
        return redirect('index')




