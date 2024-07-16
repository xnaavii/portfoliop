from django.shortcuts import render
from .models import Experience


# Create your views here.
def display_experience(request):

    experience = Experience.objects.all()
    context = {"experience": experience}
    return render(request, "portfolio/index.html", context)
