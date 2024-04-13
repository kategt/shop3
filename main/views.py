from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Categories


# Create your views here.
def index(request):

    context = {
        'title': 'Главная',
        'content': 'Магазин мебели Home',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home- О нас',
        'content': 'О нас',
        'text_on_page': 'Текс о том почему этот магазин такой классный',
    }
    return render(request, 'main/about.html', context)
