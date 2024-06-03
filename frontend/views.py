from django.shortcuts import render

def index(request):
    return render(request, 'frontend/index.html')

def login(request):
    return render(request, 'frontend/login.html')

def signup(request):
    return render(request, 'frontend/signup.html')

def docs(request):
    return render(request, 'frontend/docs.html')

def dev(request):
    return render(request, 'frontend/developer.html')

def url_redirection(request):
    
    return render(request, 'frontend/developer.html')