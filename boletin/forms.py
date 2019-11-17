from django import forms 
from .models import Registrados

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrados
        fields = ["nombre","email"]
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveedor = email.split("@")
        dominio, extension = proveedor.split(".")
        if not extension == "edu":
            raise forms.ValidationError("Por favor utiliza un emeail con la extension .EDU")
        return email

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")


class ContactForm(forms.Form):
     nombre = forms.CharField(required=False)
     email = forms.EmailField()
     mensaje = forms.CharField(widget=forms.Textarea)       