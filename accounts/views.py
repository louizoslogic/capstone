from django.shortcuts import render, reverse
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
import urllib.request
import urllib.error
from json import loads
from match.views import update_database
import os
from django.contrib import messages


def is_os():
    if 'api_key' in os.environ:
        return os.environ["api_key"]

    else:
        from secret import api_key
        return api_key


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

    try:
        with urllib.request.urlopen(f'https://{user.region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{remove_spaces(user.summonername)}?api_key={is_os()}') as response:
            html = response.read()
            data = loads(html)
            user.accountId = data["accountId"]
            user.puuid = data["puuid"]
            update_database(user)

    except urllib.error.HTTPError:
        user.delete()
        messages.info(request, 'We had an error authenticating your Riot account')
        return HttpResponseRedirect(reverse('accounts:signup'))

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
