import datetime

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q

from blog.models import Post, PostRating
from blog.forms import PostCreationForm

from braces.views import LoginRequiredMixin


class MyPostsListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        qs = super(MyPostsListView, self).get_queryset()
        qs = qs.filter(author_id=self.request.user.id)
        return qs


class PostsIndexListView(ListView):
    model = Post
    template_name = 'blog/index.html'

    def get_queryset(self):
        qs = super(PostsIndexListView, self).get_queryset()
        qs = qs.filter(Q(is_active=True) &
                       Q(publication_date__lte=datetime.datetime.now()))
        qs = qs.order_by('-publication_date')[:7]
        return qs


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['rating'] = PostRating.objects.filter(Q(user=self.request.user.username) &
                                                      Q(post=pk))
        return context


class PostCreationView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_creation.html'
    form_class = PostCreationForm

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super(PostCreationView, self).form_valid(form)

    def form_invlaid(self, form):
        form = PostCreationForm(instance=form)
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk, })


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'blog/post_update.html'

    def get_success_url(self):
        return reverse('post_list')


def activate_post(request, *args, **kwargs):
    post = get_object_or_404(Post, id=kwargs['pk'])
    post.is_active = not post.is_active
    post.save()
    return HttpResponseRedirect(reverse('post_list'))


def rate(request, **kwargs):
    if request.method == "POST":
        if request.user.is_authenticated():
            rating, is_created = PostRating.objects.get_or_create(
                user=request.user.username,
                post=kwargs['pk'],
                ip_address=request.META['REMOTE_ADDR'],)
            rating.value = request.POST['rating']
            rating.save()
        else:
            rating, is_created = PostRating.objects.get_or_create(
                user='',
                post=kwargs['pk'],
                ip_address=request.META['REMOTE_ADDR'],)
            rating.value = request.POST['rating']
            rating.save()
    return HttpResponseRedirect(reverse('post_detail',
                                        kwargs={'pk': kwargs['pk']}))
