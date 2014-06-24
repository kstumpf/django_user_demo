from django import forms
from models import UserProfile

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        # Don't need to display user in fields because we presume the user is already logged in.
        fields = ('likes_cheese', 'favorite_hamster_name')        
