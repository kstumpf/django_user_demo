from django.conf.urls import patterns, url

from .views import post_list, post_detail

urlpatterns = patterns('',
    url(r'^all/$', post_list, name='list'),
    url(r'^blog/(?P<pk>\d+)/$', post_detail, name='detail'),
#    url(r'^(?P<slug>[\w-]+)/$', 'microblog.views.blog_detail', name = 'detail'),
    url(r'^language/(?P<language>[a-z\-]+)/$', 'microblog.views.language'),
    url(r'^create/$', 'microblog.views.create', name='create'),
    url(r'^edit/(?P<pk>\d+)/$', 'microblog.views.edit', name='edit'),
    url(r'^search/$', 'microblog.views.search_titles'),
)
