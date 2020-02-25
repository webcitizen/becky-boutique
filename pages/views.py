from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, "home.html",{})

def bag(request):
	return render(request, "bags.html",{})

def shoe(request):
	return render(request, "shoes.html",{})

def men(request):
	return render(request, "men.html",{})