from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        print(f"Name: {name}, Message: {message}")  # For now, print to console
        return HttpResponse(f"Thank you {name}! Your message has been received.")
    return render(request, 'contact.html')
