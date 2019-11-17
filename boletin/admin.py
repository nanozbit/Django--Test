# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Registrados
from .forms import RegModelForm
# Register your models here.

class AdminRegistrado(admin.ModelAdmin):
    list_display = ["email", "nombre", "timestamp"]
    form = RegModelForm
    # list_display_links = ["nombre"]
    list_filter = ["timestamp"]
    list_editable = ["nombre"]
    search_fields = ["email", "nombre"]
    # class Meta:"Por favor utiliza un email con la extencion .EDU"
    #     model = Registrados

admin.site.register(Registrados, AdminRegistrado)