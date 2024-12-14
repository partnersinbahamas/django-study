from django.shortcuts import render, redirect
from .models import Article
from .form import ArticleForm

def news_main(request):
    """
    you can pick instead of objects.all() other methods such as
    objects.order_by('-key') to sort by.
    """
    data = {
        'news': Article.objects.all(),

    }
    return render(request, 'news/index.html', data)

def add_form(request):
    error = ''

    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('news-home')
        else:
            error = '! Form is invalid !'

    form = ArticleForm

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/add.html', data)
