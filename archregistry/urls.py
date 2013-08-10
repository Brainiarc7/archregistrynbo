from django.conf.urls import patterns, include, url

from archregistry.views import ArchUserListView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'archregistry.views.home', name='home'),
    # url(r'^archregistry/', include('archregistry.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', ArchUserListView.as_view(), name='home'),
)
