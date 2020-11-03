from main_app.forms import Article_Form
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import City, Author, Article
from django.contrib.auth.decorators import login_required

#---------------------ADMIN---------------------------

def signup(request):
    error_message=''

    if request.method == 'POST':
        user_form = UserCreationForm(data = {'username':request.POST['username'], 'password1': request.POST['password1'], 'password2': request.POST['password2']})
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
        return redirect('author_detail')
    else:
        error_message='Invalid sign-up try again'
    
    user_form=UserCreationForm()
    context = {'user form': user_form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def home (request):

    login_form = AuthenticationForm()

    return render(request, 'home.html', {'form': login_form})

#----------------------Cities---------------------------
@login_required
def cities_index(request):
    cities = City.objects.all()
    return render(request, 'cities/index.html', { 'cities' : cities })


@login_required
def city_detail(request, city_id):
    city = City.objects.get(id=city_id)
    return render(request, 'cities/detail.html', { 'city' : city })

#----------------------Authors-------------------------------
@login_required
def authors_index(request):
    authors = Author.objects.all()
    return render(request, 'authors/index.html', { 'authors' : authors })

@login_required
def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'authors/detail.html', { author : author })

