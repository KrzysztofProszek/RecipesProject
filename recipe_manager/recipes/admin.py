from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Ingredient)
admin.site.register(models.Chef)
admin.site.register(models.Categorie)
admin.site.register(models.Recipe)
