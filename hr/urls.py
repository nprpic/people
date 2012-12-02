from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'skeletor.views.home', name='home'),
    # url(r'^skeletor/', include('skeletor.foo.urls')),

    url(r'^contracts$', 'hr.views.contracts'),
    url(r'^absences$', 'hr.views.absences'),

)

# Note: this only gets activated if DEBUG = True
urlpatterns += staticfiles_urlpatterns()