from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from minisite.apps.blog import views
from minisite.apps import info

from solid_i18n.urls import solid_i18n_patterns

urlpatterns = patterns(
  '',
  url(r'^i18n/', include('django.conf.urls.i18n')),
  url(r'^invite/', 'info.views.invite', name='invite_page')
  )

urlpatterns += solid_i18n_patterns(
  '',
  url(r'^info/', include('info.urls')),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^blog/', include('blog.urls')),
  url(r'^$', views.PostsIndexListView.as_view(), name='index'),
  url(r'^ckeditor/', include('ckeditor.urls')),

  )
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns(
      '',
      url(r'^rosetta/', include('rosetta.urls')),
    )
