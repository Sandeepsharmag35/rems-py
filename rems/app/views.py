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


def rentpage(request):
    return render(request, 'rent.html')


def contactpage(request):
    return render(request, 'contact.html')


def propertyDetailsPage(request):
    return render(request, 'property-detail.html')


def registerpage(request):
    if request.method == 'POST':
        fullname = request.POST['form_name']
        email = request.POST['form_email']
        pass1 = request.POST['form_password']
        pass2 = request.POST['form_cpassword']

        if pass1 != pass2:
            return HttpResponse("Password did not match")

        else:
            myuser = User.objects.create_user(fullname, email, pass1)
            myuser.save()
            return redirect('loginform')

    return render(request, 'register.html')


def loginpage(request):
    if request.method == 'POST':
        email_id = request.POST['form_email']
        pass1 = request.POST['form_password']
        user = authenticate(request, email_id=email_id, password=pass1)

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
def sellpage(request):
    user = request.user
    context = {'user' = user}
    return render(request, 'sell.html')
