from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from favor_exchange.forms import FavorRequestForm, AddCreditForm
from favor_exchange.models import ExchangeUser, Token


def homepage(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            exuser = ExchangeUser()
            exuser.user = user
            exuser.save()

            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def favor_request(request):
    if request.method == 'POST':
        form = FavorRequestForm(request.POST)
        if form.is_valid():
            send_user = request.user.exchangeuser
            receive_user = User.objects.get(username=form.cleaned_data.get('user')).exchangeuser

            if not send_user.user.username == receive_user.user.username:
                send_user.credit -= 1
                send_user.save()

                receive_user.credit += 1
                receive_user.save()

    else:
        form = FavorRequestForm()
    return render(request, 'favor_request.html', {'form': form})


def add_credit(request):
    if request.method == 'POST':
        form = AddCreditForm(request.POST)
        if form.is_valid():
            user = request.user.exchangeuser
            token = Token.objects.get(token=form.cleaned_data.get('token'), used=False)

            token.used = True
            token.save()

            user.credit += token.amount
            user.save()
    else:
        form = AddCreditForm()

    return render(request, 'add_credit.html', {'form': form})
