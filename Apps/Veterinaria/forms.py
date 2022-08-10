from contextlib import nullcontext
from django import forms


vac1 = [(" Antirabica"," Antirabica"),(" Parvovirus"," Parvovirus"),(" Distemper"," Distemper"),(" Leptospirosis"," Leptospirosis")]
vac2 = [(" Antirabica"," Antirabica"),(" Parvovirus"," Parvovirus"),(" Distemper"," Distemper"),(" Leptospirosis"," Leptospirosis")]
Desparasitado = [(' Si',' Si'),(' No',' No')]
Castrado = [(' Si',' Si'),(' No',' No')]


class Ficha_form (forms.Form):
    
    registro = forms.IntegerField(label='Registro numero:',widget=forms.TextInput(attrs={'placeholder':'Ingrese número entero'}))
    vacuna_1 = forms.ChoiceField(choices=vac1,required=True,label='Vacuna numero 1')
    vacuna_2 = forms.ChoiceField(choices=vac2,required=True,label='Vacuna numero 2')
    desparasitacion = forms.ChoiceField(choices=Desparasitado,required=True,label='Desparasitado')
    castracion = forms.ChoiceField(choices=Castrado,required=True,label='Castrado')
    observaciones = forms.CharField(max_length= 200,widget=forms.TextInput(attrs={'placeholder':'Ingrese texto'}))


