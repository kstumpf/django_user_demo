# Allows us to render template back to browser.
from __future__ import unicode_literals
from django.shortcuts import render_to_response, render
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required


def home(request):
    if (request.user.is_authenticated()):
        return render(request, 'home.html')
    return login(request, template_name='home.html')
