from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_view(request):
    return render(request,'website/index.html') # automatically goes and find from templates folder

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    return render(request,'website/contact.html')

def test_view(request):
    context = {
        'name' : 'Pedram',
        'lastname': 'Pourhakim'
    }
    return render(request,'website/test.html',context)