from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from forms import UserProfileForm
from django.contrib.auth.decorators import login_required # allow you to add on utility to functions you've already created.

@login_required
def profile(request):
    if request.method == 'POST':
        # Create user profile form with post data we are about to save.
        # We want to populate form with original instance of profile.
        # Then insert post info on top of that.
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        user = request.user # request stores current logged in user.
        profile = user.profile # from user we get profile. Triggers line of code from models.
        form = UserProfileForm(instance=profile) # This will prepopulate with any existing data.

    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    args['user'] = request.user
        
    return render_to_response('profile.html', args)
