from django.shortcuts import render, get_object_or_404
from pydoc import locate
from .models import Card, Version, JOB_CHOICE, RARITY_CHOICE


def index(request):
    all_cards = Card.all_cards()
    context = {
        'all_cards': all_cards
    }
    return render(request, 'hs/index.html', context)


def detail(request, real_type_name, real_id):
    real_type = locate('hs.models.' + real_type_name)
    card = get_object_or_404(real_type, pk=real_id)
    job_value = card.job
    rarity_value = card.rarity
    pub_version_value = card.pub_version
    job = JOB_CHOICE.__getitem__(job_value - 1)[1]
    rarity = RARITY_CHOICE.__getitem__(rarity_value - 1)[1]
    cost = card.cost
    effect = card.effect
    explanation = card.explanation
    context = {
        'card_name': card.name,
        'card_job': job,
        'card_rarity': rarity,
        'card_cost': cost,
        'card_effect': effect,
        'card_explanation': explanation
    }
    return render(request, 'hs/detail.html', context)
