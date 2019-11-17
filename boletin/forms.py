from django import forms 
from .models import Registrados

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrados
        fields = ["email","nombre"]
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveedor = email.split("@")
        dominio, extension = proveedor.split(".")
        if not extension == "edu":
            raise forms.ValidationError("Por favor utiliza un emeail con la extension .EDU")
        return email



class RegForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()

