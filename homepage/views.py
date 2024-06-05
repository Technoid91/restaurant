from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from .forms import NewsForm
from .models import New

# Create your views here.


def news_carousel(request):
    """
    renders the homepage with news
    represented as a carousel
    """

    all_news = New.objects.all().order_by('-posted_on')[:5]
    all_news = [(index, news) for index, news in enumerate(all_news, start=0)]
    return render(request, 'homepage/index.html', {'all_news': all_news})


def add_news(request):
    """ View to add news to the home page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added news!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add news. Please ensure the form is valid.')
    else:
        form = NewsForm()

    template = 'homepage/add_news.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def edit_news(request, new_id):
    """ Edit material of the selected news """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    news = get_object_or_404(New, pk=new_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated news!')
            return redirect('home')
        else:
            messages.error(request, 'Failed to update news. Please ensure the form is valid.')
    else:
        form = NewsForm(instance=news)

    template = 'homepage/edit_news.html'
    context = {
        'form': form,
        'news': news,
    }
    return render(request, template, context)


def delete_news(request, new_id):
    """ Delete news from the homepage """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    news = get_object_or_404(New, pk=new_id)
    news.delete()
    messages.success(request, 'News deleted!')
    return redirect(reverse('home'))
