from django.shortcuts import render, render_to_response
from django.views.generic import ListView, DetailView
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import permission_required, login_required

# create view
from forms import PostForm
from django.core.context_processors import csrf


def post_list(request, *args, **kwargs):
    '''Displays all posts currently in the database.'''
    post_list = Post.objects.filter(published=True)

    context = {}
    context.update(csrf(request))

    context['posts'] = Post.objects.all()
    context['post_list'] = post_list
    context['user'] = request.user

    return render_to_response('post_list.html', context)


def post_detail(request, pk, *args, **kwargs):
    '''Displays detailed info about the currently selected post, given its pk.'''
    post = Post.objects.get(pk=pk, published=True)

    context = {}
    context['post'] = post
    context['user'] = request.user

    return render_to_response('post_detail.html', context)


@login_required
def create(request):
    '''Creates new model object using django forms.'''
    if request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/all/") # hardcoded url makes me nervous
    else:
        form = PostForm()
    context = {}
    context.update(csrf(request))

    context['form'] = form
    context['author'] = request.user
    context['user'] = request.user

    return render_to_response('create_post.html', context)


@login_required
def edit(request, pk):
    '''Edits model object found in the database.'''
    my_post= Post.objects.get(pk = pk)
    if request.POST:
        form = PostForm(request.POST, instance = my_post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/all/")
    else:
        form = PostForm(instance = my_post)

    context = {}
    context.update(csrf(request))
    context['form'] = form
    context['pk'] = pk
    context['user'] = request.user
    
    return render_to_response('edit_post.html', context)


def search_titles(request):
    '''Called by ajax in order to retrieve the correct objects asynchronously.'''
    if request.method == "POST":
        # Will presume there is a search_text var in POST dict and pass through.
        search_text = request.POST['search_text']
    else:
        # If not, set equal to empty string.
        search_text = ''

    posts = Post.objects.filter(title__contains=search_text)

    return render_to_response('ajax_search.html', {'posts' : posts})


class PublishedPostsMixin(object):
    def get_queryset(self):
        return self.model.objects.live()


# class PostListView(PublishedPostsMixin, ListView):
#     '''Displays a list of all current posts in the database.'''
#     model = Post


# class PostDetailView(PublishedPostsMixin, DetailView):
#     '''Displays details for currently selected post.'''
#     model = Post
