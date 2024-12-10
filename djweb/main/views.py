from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        'buttons': ['Button-1', 'Button-2', 'Button-3'],
        'buttonClass': 'btn-danger'
    }
    return render(request, 'main/index.html', data)

def about(request):
    data = {
      'text': 'This page will contain a certain amount of text that describes information about the web page.',
      'buttons': ['Click me'],
      'buttonClass': 'btn-warning'
    }
    return render(request, 'main/about.html', data)
