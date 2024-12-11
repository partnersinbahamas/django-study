from django.shortcuts import render
from .models import Article

def news_main(request):
    """
    you can pick instead of objects.all() other methods such as
    objects.order_by('-key') to sort by.
    """
    data = {
        'news': Article.objects.all(),

    }
    return render(request, 'news/index.html', data)
