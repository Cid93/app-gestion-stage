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

    url(r'^/?$',"gestionStage.views.show_main", name="accueil"),

    url(r'^entreprise/', include('entreprise.urls')),

    url(r'^stage/', include('stage.urls')),

    url(r'^visiter/$', "entreprise.views.show_visiter", name="visiter"),

    url(r'^login/$', "gestionStage.forms.login_page", name="login"),

    url(r'^logout/$', "gestionStage.forms.logout_action", name="logout"),

    url(r'^oups/$',"gestionStage.views.oups",name="oups"),

    url(r'^recherche/$',"gestionStage.views.search",name="search"),


)
