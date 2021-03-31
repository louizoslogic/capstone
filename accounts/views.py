from django.shortcuts import render, reverse
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
import urllib.request
from json import loads
from match.views import update_database
import os


# Create your views here.
def signup(request):

    return render(request, 'accounts/signup.html')


def register(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    region = request.POST['region']
    summonername = request.POST['summonername']

    user = CustomUser.objects.create_user(
        username=username,
        email=email,
        password=password,
        region=region,
        summonername=summonername
        )

    def remove_spaces(string):
        return string.replace(" ", "%20")

    with urllib.request.urlopen(f'https://{user.region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{remove_spaces(user.summonername)}?api_key={os.environ["api_key"]}') as response:
        html = response.read()
        data = loads(html)
        user.accountId = data["accountId"]
        user.puuid = data["puuid"]

    user.save()

    update_database(user)

    # redirect user to a loading screen to submit the database request
    return HttpResponseRedirect(reverse('accounts:login'))



def login_page(request):

    return render(request, 'accounts/login.html')


def login_form(request):
    
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect(reverse('match:match'))
    else:
        # Return an 'invalid login' error message.
        return HttpResponseRedirect(reverse('accounts:login'))


def home(request):
    return render(request, 'match.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('match:match'))
