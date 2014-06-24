from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^profile/$', 'userprofile.views.profile', name = 'profile'),
)
