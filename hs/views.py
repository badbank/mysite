from django.shortcuts import render, get_object_or_404
from pydoc import locate
from .models import Card, Version, JOB_CHOICE, RARITY_CHOICE, MINION_TYPE_CHOICE


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
    card_pub_version = card.pub_version
    job = JOB_CHOICE.__getitem__(job_value - 1)[1]
    rarity = RARITY_CHOICE.__getitem__(rarity_value - 1)[1]
    cost = card.cost
    effect = card.effect
    explanation = card.explanation
    image_location = 'hs/images/' + real_type_name + str(real_id) + '.png'
    if real_type_name == 'Minion':
        type_name = '随从'
        type_value = card.type
        minion_type = MINION_TYPE_CHOICE.__getitem__(type_value - 1)[1]
        context_of_single_type = {
            'minion_attack': card.attack,
            'minion_health': card.health,
            'minion_type': minion_type
        }
    elif real_type_name == 'Magic':
        type_name = '法术'
        context_of_single_type = {}
    elif real_type_name == 'Weapon':
        type_name = '武器'
        context_of_single_type = {
            'weapon_attack': card.attack,
            'weapon_durability': card.durability
        }
    else:
        type_name = '英雄'
        if card.skill_cost == -1:
            dk_skill_cost = '被动'
        else:
            dk_skill_cost = card.skill_cost
        context_of_single_type = {
            'dk_skill_cost': dk_skill_cost,
            'dk_skill_name': card.skill_name,
            'dk_skill': card.skill
        }
    context_of_all = {
        'image_location': image_location,
        'card_id': real_id,
        'card_name': card.name,
        'card_job': job,
        'card_rarity': rarity,
        'card_type': type_name,
        'card_cost': cost,
        'card_effect': effect,
        'card_explanation': explanation,
        'card_pub_version': card_pub_version,
        'card_real_type': real_type_name,
        'card_is_normal': card.is_normal()
    }
    context = {**context_of_all, **context_of_single_type}
    return render(request, 'hs/detail.html', context)
