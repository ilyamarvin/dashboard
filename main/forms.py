from django import forms
from django.db.models import fields
from .models import *

class AddAdForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = '__all__'

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewsOnUser
        fields = ['review_text', 'rating']


class UpdateAdForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = ['id_category', 'id_subcategory', 'id_location', 'name', 'description', 'link_to_photos', 'price']