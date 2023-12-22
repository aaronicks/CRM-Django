from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Customer

# Create your views here.


def home_user(request):
	# querrying the database
	records = Customer.objects.all()

	# check to see if they are login
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Logged In Successfully")
			return redirect('home')
		else:
			messages.success(request, "Loggin Error, Please Try Again Later")
			return redirect('home')
	else:
		return render(request, 'home.html', {"records":records})



def logout_user(request):
	logout(request)
	return redirect('home')



def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST or None)
		if form.is_valid():
			form.save()

			# get authenticated
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']

			user = authenticate(request, username=username, password=password)
			login(request, user)
			messages.success(request, 'You Have Successfully Registered!')
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, "register_user.html", {"form":form})

	return render(request, "register_user.html", {"form":form})
			



def customer_record(request, pk):

	if request.user.is_authenticated:
		# look up record
		customer_record = Customer.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, 'You Must Be Logged In To View That Page...')
		return redirect('home')


def delete_record(request, pk):
	if request.user.is_authenticated:
		# look for the database
		delete_it = Customer.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, 'Record Deleted Successfully.....')
		return redirect("home")
	else:
		messages.success(request, 'You Must Be Logged In To Do That.....')
		return redirect("home")


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == 'POST':
			if form.is_valid():
				form.save()
				messages.success(request, 'You Have Successfully Added New Account...')
				return redirect('home')
		return render(request, 'add_record.html', {"form":form})
	else:
		messages.success(request, 'You Must Be Logged In To Do That....')
		return redirect('home')





def update_record(request, pk):
	if request.user.is_authenticated:
		record = Customer.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=record)
		if form.is_valid():
			form.save()
			messages.success(request, 'Record Has Been Updated!')
			return redirect('home')
		return render(request, 'update_record.html', {"form":form})
	else:
		messages.success(request, 'You Need To Be Logged In To Do That!!')
		return redirect('home')