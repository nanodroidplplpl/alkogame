from django import forms
from .models import Sesje, Gracze

class PostScoreForm(forms.Form):
    g_nick = forms.CharField(label='name', max_length = 200)
    score = forms.IntegerField()
