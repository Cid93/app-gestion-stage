from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gestionStage.views.home', name='home'),
    # url(r'^gestionStage/', include('gestionStage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
   
    url(r'^/?$',"stage.views.show_stages"),

)