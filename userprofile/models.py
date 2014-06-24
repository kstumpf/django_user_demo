from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    # Want to tie in the relationship between this model & user model
    # and only have one relationship so one user can only have one user profile.
    user = models.OneToOneField(User)
    # Now we'll add in the extra fields!
    likes_cheese = models.BooleanField(default = False)
    favorite_hamster_name = models.CharField(max_length=50)

# User needs a profile property.
# Whenever you pass in user object to this property
# it runs through objects of UserProfile model and run get_or_create.
# If it is in the database it gets it, if not it creates it.
# Should automatically populate the user.profile (when user made) with a newly created profile.
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

# Now we create a forms.py to edit this info with.
