# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import RegModelForm, ContactForm
from .models import Registrados
# Create your views here.

def inicio(request):
    titulo = "hola"
    if request.user.is_authenticated():
        titulo = "Bienvenido %s" %(request.user)

    form = RegModelForm(request.POST or None)
    context = {
        "el_form": form,
        "titulo" : titulo,
    }

    if form.is_valid():
        form_data = form.cleaned_data
        nombre = form_data.get("nombre")
        email = form_data.get("email")
        instance = form.save(commit=False)
        instance.save() 
        print instance.timestamp
        # obj = Registrados.objects.create(email = email, nombre = nombre)
        context = {
            "titulo" : "Gracias %s!" %(email)
        }
        if not nombre:
            context = {
                "titulo": "Gracias %s" %(email)
            }
    return render(request, "index.html", context)
 

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        mensaje = form.cleaned_data.get("mensaje")
        nombre = form.cleaned_data.get("nombre")
        print email, mensaje, nombre
        #for key,value in form.cleaned_data.iteritems()
    context = {
        "form": form,
    }
    return render(request, "forms.html", context)

