# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Registrados
# Register your models here.

class AdminRegistrado(admin.ModelAdmin):
    list_display = ["email", "nombre",  "timestamp"]
    # list_display_links = ["nombre"]
    list_filter = ["timestamp"]
    list_editable = ["nombre"]
    search_fields = ["email","nombre"]
    class Meta:
        model = Registrados

admin.site.register(Registrados, AdminRegistrado)