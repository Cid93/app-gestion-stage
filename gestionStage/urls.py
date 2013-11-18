from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gestionStage.views.home', name='home'),
    # url(r'^gestionStage/', include('gestionStage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$',"entreprise.views.show_main"),
    url(r'^company/?$',"entreprise.views.show_entreprise"),
    url(r'^addEnt/$',"entreprise.views.addEnt"),
    url(r'^company/(\d+)$',"entreprise.views.show_detail_entreprise"),
    url(r'^delete/(\d+)$',"entreprise.views.delEnt"),

)
