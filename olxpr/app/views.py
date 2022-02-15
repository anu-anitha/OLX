from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . forms import SignupForm

# Create your views here.
@login_required(login_url='login')
def home(request):
	return render(request,'home.html')

def base(request):
	return render(request,'base.html')

def loginn(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username = username,password = password)
		if user is not None:
			login(request,user)
			if request.user.is_authenticated:
				username = request.user.username
				messages.info(request, "Welcome "+username)
			return redirect('/app/home')
	return render(request, 'login.html')



def signup(request): 
	form = SignupForm() 
	if request.method == 'POST':#TRUE

		print(request.POST) 
		form = SignupForm(request.POST) 
		if form.is_valid():	
			form.save()
	context = {'form':form}
	return render(request, 'signup.html', context)


