'''
Created on Sep 19, 2013

@author: arvind
'''

from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from registration.backends.default.views import RegistrationView

urlpatterns = patterns('',
                       #Custom information Screens @author: arvind
                       #default site register page
                       url(r'^$',
                           RegistrationView.as_view(),
                           name='registration_register'),
                       url(r'^about/$',
                           TemplateView.as_view(template_name='registration/about_us.html'),
                           name='about_us'),
                       url(r'^contact/$',
                           TemplateView.as_view(template_name='registration/contact_us.html'),
                           name='contact_us'),
                       url(r'^home/$',
                           TemplateView.as_view(template_name='registration/artiste_home.html'),
                           name='nav_home'),
                       )
                        
