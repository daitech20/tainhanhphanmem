from django import forms
from .models import DataTable

class CodeForm(forms.Form):
    code = forms.CharField(max_length=10, label=False, widget=forms.TextInput(attrs={'placeholder': 'Bạn cần nhập Pass'}))