from django import forms
from .models import newsweek

class NewsweekCreateForm(forms.ModelForm):
    class Meta:
        model = newsweek
        fields = ('author', 'Title', 'created')