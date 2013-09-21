from django.conf.urls import patterns, include

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'artiste.views.home', name='home'),
    # url(r'^artiste/', include('artiste.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls',namespace="accounts")),
    (r'^', include('registration.auth_urls',namespace="artiste_auth")),
    #urls for the website navigation
    (r'^', include('registration.nav_urls',namespace="navigation")),
)
