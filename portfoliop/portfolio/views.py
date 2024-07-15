from django.shortcuts import render

# Create your views here.
def index(request):

    title = "Hello World"
    context = {"title": title}

    return render(request, 'portfolio/index.html', context)