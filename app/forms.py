from app.models import csv,txt
from django import forms

class CsvModelForm(forms.ModelForm):
        class Meta:
            model = csv
            fields = ('file_name',)
        def __init__(self, *args, **kwargs):
            super(CsvModelForm, self).__init__(*args, **kwargs)
            self.fields['file_name'].widget.attrs.update({'class': ''})

class txtform(forms.ModelForm):
        class Meta:
            model = txt
            fields = ('file_name',)
        def __init__(self, *args, **kwargs):
            super(txtform, self).__init__(*args, **kwargs)
            self.fields['file_name'].widget.attrs.update({'class': ''})