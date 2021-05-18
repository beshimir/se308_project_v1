





from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm

# Create your views here.





def home(request):
	return render(request, 'accounts/dashboard.html')

def login(request):
	context = {}
	return render(request, 'accounts/login.html', context)

def register(request):
	form = CreateUserForm();

	if request.method == 'POST':
		form = CreateUserForm(request.POST);
		if form.is_valid():
			form.save()
		novalidate = True

	context = {'form':form}
	return render(request, 'accounts/register.html', context)

