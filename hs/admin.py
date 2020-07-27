from django.contrib import admin
from .models import Spell, Minion, Hero, Weapon, Version, Skill, Job, Rarity, MinionType


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
    list_filter = ['job',
                   'pub_version',
                   'cost',
                   'attack',
                   'health',
                   'type',
                   'rarity']
    search_fields = ['name', 'effect', 'explanation']


class SpellAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'job',
                    'rarity',
                    'cost',
                    'effect',
                    'explanation',
                    'pub_version')
    list_filter = ['job', 'pub_version', 'cost', 'rarity']
    search_fields = ['name', 'effect', 'explanation']


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
    list_filter = ['job',
                   'pub_version',
                   'cost',
                   'rarity',
                   'attack',
                   'durability']
    search_fields = ['name', 'effect', 'explanation']


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
    list_filter = ['job',
                   'pub_version',
                   'cost',
                   'armor',
                   'skill_cost',
                   'rarity']
    search_fields = ['name', 'effect', 'explanation', 'skill_name', 'skill']


class VersionAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'pub_date',
                    'is_normal',
                    'ordering')
    list_filter = ['pub_date']
    search_fields = ['name']


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


class JobAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color'
    )


class RarityAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'color',
                    'has_dragon')


class MinionTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Minion, MinionAdmin)
admin.site.register(Spell, SpellAdmin)
admin.site.register(Hero, HeroAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Version, VersionAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Rarity, RarityAdmin)
admin.site.register(MinionType, MinionTypeAdmin)
