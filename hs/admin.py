from django.contrib import admin
from .models import Magic, Minion, Dk, Weapon, Version

admin.site.register(Minion)
admin.site.register(Magic)
admin.site.register(Weapon)
admin.site.register(Dk)
admin.site.register(Version)
