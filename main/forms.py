from django import forms
from .models import *

class AddAdForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = '__all__'

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'

class AboutWorkers(forms.ModelForm):
    class Meta:
        model = Workers
        fields = '__all__'