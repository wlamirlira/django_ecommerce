from django.http import HttpResponse
from django.shortcuts import render

def home_pages(request):
    context = {
        "title": "Página Principal",
        "content": "Bem-Vindo a página principal"
    }
    return render(request, 'home.html', context)

def about_page(request):
    context = {
        "title": "Página Principal - ABOUT PAGE",
        "content": "Bem-Vindo a página principal"
    }
    return render(request, 'about/view.html', context)

def contact_page(request):
    context = {
        "title": "Página Principal - CONTACT PAGE",
        "content": "Bem-Vindo a página principal"
    }
    return render(request, "contact/view.html", context)