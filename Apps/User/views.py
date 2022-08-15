
from http.client import HTTPResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render,redirect

from Apps.User.models import User_profile
from Apps.User.forms import User_profile_Form, UserEditForm, User_registration_form,UserEditPerfilForm



def padre (request):
    return render (request, "padre.html")

def index (request):
    return render (request, "index.html")

def inicio (request):
    return render(request, "inicio.html")

def en_construccion (request):
    return render (request, "en_construccion.html")

def respuesta (request):
    return render (request, "User/respuesta.html")

#######################################################################


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

#####################################################################

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

################################################################################

def logout_view(request):
    logout(request)
    return render(request, "User/respuesta.html",{"context":f"Cerraste sesión"})


##################################################################################

# def crear_profile(request): 

#     if request.method=='GET':

#         form = User_profile_Form()
#         context = {
#         'form' : form,
#         }
#     else:
#         form = User_profile_Form(request.POST, request.FILES)
#         if form.is_valid():
#             nueva_perfil = User_profile.objects.create(
#                     user = request.user,
#                     phone = form.cleaned_data['phone'],
#                     nombre = form.cleaned_data['nombre'],
#                     apellido = form.cleaned_data['apellido'],
#                     correo = form.cleaned_data['correo'],
#                     profile_image = form.cleaned_data['profile_image']
#             )
#             return redirect('gestion-peñon')
#     return render(request,'auth/crear_profile.html',context)

# ##########################################################################

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

# ###################################################################################


def eliminar_profile(request,id):

    profile = get_object_or_404(User_profile,user=request.user)

    if request.method == 'GET':
        mensaje = 'Esta por borrar el perfil'
        form = User_profile_Form(instance=profile)
        context = {'form':form,'mensaje':mensaje}
        return render (request,'User/del_profile.html',context)
    else:
        profile.delete()
        return redirect('index')

# ###################################################################################



@login_required
def show_perfil (request):

    if request.user.is_authenticated:

        # return HttpResponse (request.user.profile.phone)

        usuario = (
            request.user.profile.first_name,
            request.user.profile.last_name,
            request.user.profile.phone,
            request.user.profile.direccion,
            request.user.profile.description,
            request.user.profile.image
          )


    return render(request, 'User/profile.html', {"usuario":usuario})





# @login_required
# def edit_user (request, id):

#     usuario= request.user

#     if request.method == "POST":
        
#         miFormulario= UserEditPerfilForm(request.POST, instance=request.user)

#         if miFormulario.is_valid():

#             info= miFormulario.cleaned_data

#             usuario.email= info["email"]
#             usuario.first_name= info["first_name"]
#             usuario.last_name= info["last_name"]
            
#             usuario.save()

#             return redirect("index")

#     else:

#         miFormulario= UserEditPerfilForm(instance=request.user)

#         return render (request, "User/edit_profile.html", {"miFormulario":miFormulario, "usuario":usuario})


# @login_required
# def edit_perfil (request, id):

#     # usuario= request.user
#     profile = User_profile.objects.get(id=id)

#     if request.method == "POST":
        
#         miFormulario= UserEditPerfilForm(request.POST)

#         if miFormulario.is_valid():

#             info= miFormulario.cleaned_data

#             profile.first_name= info["first_name"]
#             profile.last_name= info["last_name"]
#             profile.phone= info["phone"]
#             profile.address= info["address"]
#             profile.direccion= info["direccion"]
#             profile.description= info["description"]
#             # profile.image= info["image"]

#             profile.save()

#             return redirect("perfil")

#     else:

#         miFormulario= UserEditPerfilForm(initial={
#             "first_name": profile.first_name,
#             "last_name": profile.last_name,
#             "phone": profile.phone,
#             "address": profile.address,
#             "direccion": profile.direccion,
#             "description": profile.description,
#             # "image": profile.image,
        
#          }
#         )       

#         return render (request, "User/edit_profile.html", {"miFormulario":miFormulario, "id":profile.id})



@login_required
def create_perfil(request):

    if request.method == "POST":
     
        form = User_profile_Form(request.POST, request.FILES)

        if form.is_valid():

            User_profile.objects.create(

                    user = request.user,
                    first_name = form.cleaned_data['first_name'],
                    last_name = form.cleaned_data['last_name'],
                    phone = form.cleaned_data['phone'],
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




