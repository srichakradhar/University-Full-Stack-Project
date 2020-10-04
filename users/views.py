from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, OfficialSignUpForm

def signup_view(request):
	if request.user.is_authenticated:
		return redirect('users:home')
	if request.method == 'POST':
		try:
			userForm = SignUpForm(request.POST)
		except Exception as e:
			userForm = OfficialSignUpForm(request.POST)

		if userForm.is_valid():
			userForm.save()
			username = userForm.cleaned_data.get('username')
			password = userForm.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('users:home')
		else:
			messages.error(request, 'Correct the errors below')
	else:
		userForm = SignUpForm()
		officialForm = OfficialSignUpForm()

	return render(request, 'app/signup.html', {'userForm': userForm, 'officialForm': OfficialSignUpForm})


@login_required
def dashboard_view(request):
	return render(request, 'app/dashboard.html')

def home_view(request):
	return render(request, 'app/home.html')

def portfolio(request):
	return render(request, 'portfolio.html')

def portfolio_page(request):
	return render(request, 'portfolio-page.html')

def contact(request):
	return render(request, 'contact.html')

def about(request):
	return render(request, 'about.html')