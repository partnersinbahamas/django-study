from django.shortcuts import render

def news_main(request):
    return render(request, 'news/index.html')
