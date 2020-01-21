from django.shortcuts import render, get_object_or_404
from pydoc import locate
from .models import Card, Version


def index(request):
    all_cards = Card.all_cards()
    context = {
        'all_cards': all_cards
    }
    return render(request, 'hs/index.html', context)


def detail(request, real_type_name, real_id):
    real_type = locate('hs.models.' + real_type_name)
    card_name = get_object_or_404(real_type, pk=real_id)
    context = {
        'card_name': card_name
    }
    return render(request, 'hs/detail.html', context)
