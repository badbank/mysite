from django.shortcuts import render
from django.http import HttpResponse
from .models import Minion, Magic, Dk, Weapon, Version


def index(request):
    all_minions = list(Minion.objects.all())
    all_magics = list(Magic.objects.all())
    all_dks = list(Dk.objects.all())
    all_weapons = list(Weapon.objects.all())
    all_cards = all_minions + all_magics + all_dks + all_weapons
    context = {
        'all_cards': all_cards
    }
    return render(request, 'hs/index.html', context)


def detail(request, card_name):
    return HttpResponse("You're looking at card '%s'." % card_name)
