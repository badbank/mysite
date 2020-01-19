from django.contrib import admin
from .models import Magic, Minion, Dk, Weapon, Version, Card

admin.site.register(Minion)
admin.site.register(Magic)
admin.site.register(Dk)
admin.site.register(Weapon)
admin.site.register(Version)
