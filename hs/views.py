from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Card, Version


def index(request):
    all_cards = Card.all_cards()
    context = {
        'all_cards': all_cards
    }
    return render(request, 'hs/index.html', context)


def detail(request, real_type, real_id):
    return HttpResponse("You're looking at %s, id %s." % (real_type, real_id))
