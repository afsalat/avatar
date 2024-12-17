from django import forms
from .models import Avatar_pic

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar_pic
        fields = ['image']
