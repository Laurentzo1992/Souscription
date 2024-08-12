from django.contrib import admin
from unfold.admin import ModelAdmin
from souscription.models import *

@admin.register(Souscripteur)
class CustomAdminClass(ModelAdmin):
    pass


@admin.register(Projet)
class CustomAdminClass(ModelAdmin):
    pass


@admin.register(Souscription)
class CustomAdminClass(ModelAdmin):
    pass

