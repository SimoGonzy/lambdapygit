from django.shortcuts import render

def index(request):
    """Home page di learning logs"""
    return render(request, "learning_logs/index.html")
