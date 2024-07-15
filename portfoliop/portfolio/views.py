from django.shortcuts import render


# Create your views here.
def index(request):

    title = ("Hello World", "Apple")
    context = {"title": title}

    return render(request, "portfolio/index.html", context)
