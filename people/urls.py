from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'skeletor.views.home', name='home'),
    # url(r'^skeletor/', include('skeletor.foo.urls')),

    url(r'^$', 'core.views.index'),
    url(r'^login$', 'core.views.login_view'),
    url(r'^logout$', 'core.views.logout_view'),
    url(r'^people$', 'core.views.people'),
    url(r'^add_new_person$', 'core.views.add_new_person'),
    url(r'^save_person$', 'core.views.save_person'),
    url(r'^person_profile/(?P<person_id>\d+)$', 'core.views.person_profile'),
    url(r'^delete_person/(?P<person_id>\d+)$', 'core.views.delete_person'),
    url(r'^autocomplete$', 'core.views.autocomplete'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# Note: this only gets activated if DEBUG = True
urlpatterns += staticfiles_urlpatterns()