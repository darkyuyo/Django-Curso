from django import forms

class CreatenewAutor(forms.Form):
    nombre=forms.CharField(label="Nombre del autor",max_length=75)
    fecha_nacimiento=forms.DateField(label="Fecha de nacimiento")
    fecha_fallecimiento=forms.DateField(label="Fecha de fallecimiento",required=False)
    nacionalidad=forms.CharField(label="Nacionalidad del autor",max_length=75)
