from django.shortcuts import render

def home(request):
    return render(request, 'example.html')

def example(request):
    return render(request, 'example.html')
