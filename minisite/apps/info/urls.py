from django.conf.urls import patterns, url
from info import views
from django.contrib.auth import views as reset_views
from django.core.urlresolvers import reverse_lazy
from info import forms

urlpatterns = patterns(
  'info.views',
  url(r'^$', views.InfoDetailView.as_view(), name='info'),
  url(r'^requests_history/$', views.LatestRequestListView.as_view(),
      name='requests_history'),
  url(r'^create_info/$', views.InfoCreationView.as_view(),
      name='create_info'),
  url(r'^edit/(?P<pk>\d+)/$', views.InfoUpdateView.as_view(), name='edit'),
  url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
  url(r'^register/(?P<code>[A-Za-z]+)/$', views.InviteRegisterFormView.as_view(),
      name='invite_register'),
  url(r'^login/$', 'login_view', name='login'),
  url(r'^logout/$', views.LogoutView.as_view(), name='logout'),

  url(r'^user/password/reset/$', reset_views.password_reset,
      {'post_reset_redirect': reverse_lazy('reset_done'),
       'password_reset_form': forms.MyPasswordResetForm,},
      name="password_reset"),
  url(r'^user/password/reset/done/$',
      reset_views.password_reset_done,
      name='reset_done'),
  url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
      reset_views.password_reset_confirm,
      {'post_reset_redirect': reverse_lazy('done')},
      name='password_reset_confirm'),
  url(r'^user/password/done/$', reset_views.password_reset_complete,
      name='done'),
  )
