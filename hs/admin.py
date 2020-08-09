from django.contrib import admin
from .models import Spell, Minion, Hero, Weapon, Version, Skill, Job, Rarity, MinionType


@admin.register(Minion)
class MinionAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'get_jobs',
                    'rarity',
                    'cost',
                    'attack',
                    'health',
                    'type',
                    'effect',
                    'explanation',
                    'pub_version',
                    'is_normal')
    list_filter = ['job',
                   'pub_version',
                   'cost',
                   'attack',
                   'health',
                   'type',
                   'rarity']
    search_fields = ['name', 'effect', 'explanation']


@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'get_jobs',
                    'rarity',
                    'cost',
                    'effect',
                    'explanation',
                    'pub_version')
    list_filter = ['job', 'pub_version', 'cost', 'rarity']
    search_fields = ['name', 'effect', 'explanation']


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'get_jobs',
                    'rarity',
                    'cost',
                    'attack',
                    'durability',
                    'effect',
                    'explanation',
                    'pub_version',
                    'is_normal')
    list_filter = ['job',
                   'pub_version',
                   'cost',
                   'rarity',
                   'attack',
                   'durability']
    search_fields = ['name', 'effect', 'explanation']


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'get_jobs',
                    'rarity',
                    'cost',
                    'effect',
                    'armor',
                    'skill_cost',
                    'skill_name',
                    'skill',
                    'explanation',
                    'pub_version',
                    'is_normal')
    list_filter = ['job',
                   'pub_version',
                   'cost',
                   'armor',
                   'skill_cost',
                   'rarity']
    search_fields = ['name', 'effect', 'explanation', 'skill_name', 'skill']


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'pub_date',
                    'is_normal',
                    'ordering')
    list_filter = ['pub_date']
    search_fields = ['name']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'cost',
        'effect',
        'job',
        'pub_version'
    )
    list_filter = ['cost', 'job', 'pub_version']
    search_fields = ['name', 'effect']


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color'
    )


@admin.register(Rarity)
class RarityAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'color',
                    'has_dragon')


@admin.register(MinionType)
class MinionTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
