from django.http import HttpResponse
from django.shortcuts import render

def home_pages(request):
    context = {
        "title": "Página Principal",
        "content": "Bem-Vindo a página principal"
    }
    return render(request, 'home_page.html', context)

def about_pages(request):
    context = {
        "title": "Página Principal - ABOUT PAGE",
        "content": "Bem-Vindo a página principal"
    }
    return render(request, 'about_page.html', context)

def contact_pages(request):
    context = {
        "title": "Página Principal - CONTACT PAGE",
        "content": "Bem-Vindo a página principal"
    }
    return render(request, "contact_page.html", context)