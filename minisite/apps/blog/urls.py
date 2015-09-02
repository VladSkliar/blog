from django.conf.urls import patterns, url
from blog import views
from blog.forms import PostCreationForm


urlpatterns = patterns(
  'blog.views',
  url(r'^$', views.MyPostsListView.as_view(), name='post_list'),
  url(r'^post/(?P<pk>[-\w]+)/$',
      views.PostDetailView.as_view(), name='post_detail'),
  url(r'^create_post/$', views.PostCreationView.as_view(), name='create_post'),
  url(r'^post/(?P<pk>\d+)/update/$', views.PostUpdateView.as_view(),
      name='update_post'),
  url(r'^post/(?P<pk>\d+)/activate/$', "activate_post",
      name='activate_post'),
  url(r'^post/(?P<pk>\d+)/rate/$', "rate",
      name='rate_post')

  )
