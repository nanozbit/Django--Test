# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .forms import RegModelForm, ContactForm
from .models import Registrados
# Create your views here

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
        form_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        email_from = settings.Email_Host
        asunto = "Form contacto"
        email_to = [email_from, "otromail@gmail.com"]
        email_mensaje = " Hola como estas amiguito "

        send_mail(asunto,
        email_mensaje,
        email_from,
        email_to,
        fail_silently=False)
        #for key,value in form.cleaned_data.iteritems()
    context = {
        "form": form,
    }
    return render(request, "forms.html", context)

