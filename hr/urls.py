from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'skeletor.views.home', name='home'),
    # url(r'^skeletor/', include('skeletor.foo.urls')),

    url(r'^contracts$', 'hr.views.contracts'),
    url(r'^contracts/add$', 'hr.views.add_new_contract'),
    url(r'^contracts/(?P<contract_id>\d+)/delete$', 'hr.views.delete_contract'),
    url(r'^contracts/autocomplete$', 'hr.views.autocomplete_contract'),
    url(r'^absences$', 'hr.views.absences'),
    url(r'^absences/add$', 'hr.views.add_new_absence'),


)

# Note: this only gets activated if DEBUG = True
urlpatterns += staticfiles_urlpatterns()