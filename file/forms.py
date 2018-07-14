from django import forms
from file.models import FileModel


class FileForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = ['file']
