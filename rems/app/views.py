from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def homepage(request):
    return render(request, 'index.html')


def aboutpage(request):
    return render(request, 'about.html')


def agentspage(request):
    return render(request, 'agents.html')


def blogpage(request):
    return render(request, 'blog.html')


def blogdetailspage(request):
    return render(request, 'blogdetail.html')


def buySaleRentPage(request):
    return render(request, 'buysalerent.html')


def buypage(request):
    return render(request, 'buy.html')


def sellpage(request):
    return render(request, 'sell.html')


def rentpage(request):
    return render(request, 'rent.html')


def contactpage(request):
    return render(request, 'contact.html')


def propertyDetailsPage(request):
    return render(request, 'property-detail.html')


def registerpage(request):
    return render(request, 'register.html')


def signup(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1 != pass2:
            return HttpResponse("Password did not match")

        else:
            myuser = User.objects.create_user(uname, email, pass1)
            myuser.save()
            return redirect('loginform')

    return render(request, 'register.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return HttpResponse("Username or Password is invalid !")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('loginpage')


@login_required(login_url='login')
def home(request):
    return render(request, 'sell.html')
