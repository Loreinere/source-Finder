from django import forms
from .models import upload

class UploadCreateForm(forms.ModelForm):
    class Meta:
        model = upload
        fields = ('author', 'Title', 'created')