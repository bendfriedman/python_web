from django.shortcuts import render
from datetime import date

# Create your views here.
def home(request):
    context = {
        "site_name": "Übung 2",
        "name": request.GET.get('name') or "Ben",
        "languages": ["Python", "JavaScript", "Kotlin", "Brainfuck","Java"],
        "year": date.today().year,
    }
    return render(request, 'home.html', context)