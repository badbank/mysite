from django.contrib import admin
from .models import Magic, Minion, Dk, Weapon, Version, Card


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


class MagicAdmin(admin.ModelAdmin):
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


class DkAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'job',
                    'rarity',
                    'cost',
                    'effect',
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


admin.site.register(Minion, MinionAdmin)
admin.site.register(Magic, MagicAdmin)
admin.site.register(Dk, DkAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Version, VersionAdmin)
