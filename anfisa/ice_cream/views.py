from django.shortcuts import render


def index(request):
    template = 'ice_cream/index.html'
    context = {
        'text': 'Главная страница',
    }
    return render(request, template, context)


def ice_cream_list(request):
    template = 'ice_cream/ice_cream_list.html'
    context = {
        'text': 'Список мороженого',
    }
    return render(request, template, context)


def ice_cream_detail(request, pk):
    template = 'ice_cream/ice_cream_detail.html'
    context = {
        'text': f'Мороженое номер {pk}',
    }
    return render(request, template, context)

