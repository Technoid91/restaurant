from django.shortcuts import render
from .models import New

# Create your views here.


def news_carousel(request):

    all_news = New.objects.all()
    return render(request, 'homepage/index.html', {'all_news': all_news})
