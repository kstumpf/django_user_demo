from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from userprofile.models import UserProfile

# Override functionality of UserCreationForm to add email section.
class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        user.set_password(self.cleaned_data["password1"])

        # We automatically save unless we want to specify not to.
        if commit:
            user.save()

        return user
