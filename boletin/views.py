# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import RegForm
from .models import Registrados
# Create your views here.

def inicio(request):
    form = RegForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        email = form_data.get("email")
        nombre = form_data.get("nombre")
        obj = Registrados.objects.create(email = email, nombre = nombre)
    context = {
        "el_form": form,
    }
    return render(request, "index.html", context)
 