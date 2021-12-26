from django.forms import ModelForm, fields
from .models import Url

class MainForm(ModelForm):
    class Meta:
        model = Url
        fields = ('url',)