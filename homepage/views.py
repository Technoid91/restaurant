from django.shortcuts import render
from .models import New

# Create your views here.


def news_carousel(request):
    """
    renders the homepage with news
    represented as a carousel
    """

    all_news = New.objects.all()
    return render(request, 'homepage/index.html', {'all_news': all_news})
