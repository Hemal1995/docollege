from django import forms
from . import models
class studentForm(forms.ModelForm):
    name = forms.ChoiceField(choices=(
        ("Hiroyuki","Hiroyuki"),
        ("Shotaro","Shotaro"),
        ("Rui","Rui"),
        ("Shinnosuke","Shinnosuke"),
        ("Hito","Hito"),
        ("Aina","Aina"),
        ("Masaya","Masaya"),
        ("Kenji","Kenji"),
        ("Ryusei","Ryusei"),
        ("Kento","Kento"),
        ("Hiroshi","Hiroshi"),
        ("Shizuka","Shizuka"),
        ("Asahi","Asahi"),
    ))
    course = forms.ChoiceField(choices=(
         ("Read", "Read"),
          ("Write","Write"),
          ("Speak","Speak"),
          ("Listen", "Listen"),
          ("Grammer", "Grammer")),
          )
    class Meta: 
        model =models.student
        fields = ('name', 'course')

class startForm(forms.ModelForm):
    class Meta: 
        model = models.student
        fields = ('start_time',)

class finishForm(forms.ModelForm):
    class Meta: 
        model = models.student
        fields = ('finish_time','time_minute')