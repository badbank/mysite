from django.contrib import admin
from .models import Spell, Minion, Hero, Weapon, Version, Skill, Job


class MinionAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'job',
                    'rarity',
                    'cost',
                    'attack',
                    'health',
                    'type',
                    'effect',
                    'explanation',
                    'pub_version',
                    'is_normal')
    list_filter = ['job', 'pub_version', 'cost']
    search_fields = ['name']


class SpellAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'job',
                    'rarity',
                    'cost',
                    'effect',
                    'explanation',
                    'pub_version',
                    'is_normal')
    list_filter = ['job', 'pub_version', 'cost']
    search_fields = ['name']


class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'job',
                    'rarity',
                    'cost',
                    'attack',
                    'durability',
                    'effect',
                    'explanation',
                    'pub_version',
                    'is_normal')
    list_filter = ['job', 'pub_version', 'cost']
    search_fields = ['name']


class HeroAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'job',
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
    list_filter = ['job', 'pub_version', 'cost']
    search_fields = ['name']


class VersionAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'pub_date',
                    'is_normal')
    list_filter = ['pub_date']
    search_fields = ['name']


class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'cost',
        'effect',
        'job'
    )
    list_filter = ['cost', 'job']
    search_fields = ['name']


class JobAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color'
    )
    search_fields = ['name']


admin.site.register(Minion, MinionAdmin)
admin.site.register(Spell, SpellAdmin)
admin.site.register(Hero, HeroAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Version, VersionAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Job, JobAdmin)
