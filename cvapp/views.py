from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import PhotoForm
from .models import Photo,Profile
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'cvapp/index.html')


def signup(request):
    if request.method=='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                return render(request,'cvapp/signup.html',{'error':'Username already exists'})
            elif User.objects.filter(email=email).exists():
                return render(request, 'cvapp/signup.html', {'error': 'Email already exists'})
            else:
                user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password1)
                user.save()
                return redirect('/')
        return render(request, 'cvapp/signup.html', {'error': 'Password already exists'})
    return render(request, 'cvapp/signup.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        return render(request,'cvapp/login.html',{'error':'invalid credetial'})
    return render(request,'cvapp/login.html')

@login_required(login_url='loginform')
def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('index')


@login_required(login_url='loginform')
def getPhotos(request):
    photo=Photo.objects.filter(user=request.user)
    return render(request,'cvapp/getphoto.html',{'photo':photo})


@login_required(login_url='loginform')
def postphoto(request):
    if request.method=='POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            newform=form.save(commit=False)
            newform.user=request.user
            newform.save()
            return redirect('index')
    return render(request,'cvapp/photoform.html',{'photo':PhotoForm()})


@login_required(login_url='deletephotos/<int:id>')
def updatephoto(request,id):
    photo=Photo.objects.get(id=id)
    updatephoto=PhotoForm(request.POST or None,request.FILES, instance=photo)
    if request.method=='POST':
        if updatephoto.is_valid():
            newform=updatephoto.save(commit=False)
            newform.user=request.user
            newform.save()
            return redirect('index')
    return render(request,'cvapp/updatephoto.html',{'updatephoto':updatephoto})


@login_required(login_url='loginform')
def deletephoto(request,id):
    photo = Photo.objects.get(id=id)
    photo.delete()
    return redirect('getphotos')

@login_required(login_url='loginform')
def profile(request):
    profile=Profile.objects.filter(user=request.user)
    return render(request,'cvapp/profile.html',{'profile':profile})



