from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Item)
admin.site.register(models.Inventory)
admin.site.register(models.Ingredient)
admin.site.register(models.Entry)
