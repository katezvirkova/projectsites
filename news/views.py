from django.shortcuts import render
from .models import News, Author

def home(request):
    latest_news = News.objects.order_by('-publication_date')[:5]
    return render(request, 'news/home.html', {'latest_news': latest_news})

def news_list(request):
    all_news = News.objects.order_by('-publication_date')[:8]
    return render(request, 'news/news_list.html', {'all_news': all_news})

def news_detail(request, new_id):
    news = News.objects.get(id=new_id)
    return render(request, 'news/news_details.html', {'news': news})

def authors(request):
    all_authors = Author.objects.all()
    return render(request, 'news/authors.html', {'all_authors': all_authors})

def author_news(request, author_id):
    author = Author.objects.get(id=author_id)
    news_by_author = News.objects.filter(author=author)
    return render(request, 'news/author_news.html', {'author': author, 'news_by_author': news_by_author})
