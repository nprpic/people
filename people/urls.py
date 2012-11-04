from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'skeletor.views.home', name='home'),
    # url(r'^skeletor/', include('skeletor.foo.urls')),

    url(r'^$', 'core.views.index'),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'people/login.html'}),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', {'template_name':'people/login.html'}),
    url(r'^people$', 'core.views.people'),
    url(r'^people/add$', 'core.views.add_new_person'),
    url(r'^people/save$', 'core.views.save_person'),
    url(r'^people/(?P<user_id>\d+)$', 'core.views.person_profile'),
    url(r'^people/(?P<user_id>\d+)/delete$', 'core.views.delete_person'),
    url(r'^autocomplete$', 'core.views.autocomplete'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# Note: this only gets activated if DEBUG = True
urlpatterns += staticfiles_urlpatterns()