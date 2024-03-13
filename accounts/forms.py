from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)  # User 모델의 email 필드 추가

    class Meta:
        model = UserProfile
        fields = ['photo', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }