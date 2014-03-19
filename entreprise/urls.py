from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gestionStage.views.home', name='home'),
    # url(r'^gestionStage/', include('gestionStage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
   
	# Entreprises
    url(r'^/?$',"entreprise.views.show_entreprise"),

    # Manipulation Entreprise
    url(r'^(?P<pk>\d+)$',"entreprise.views.show_detail_entreprise",name="ent"),
    url(r'^ajouter/$',"entreprise.views.addEnt",name="addEnt"),
    url(r'^supprimer/$',"entreprise.views.delEnt",name="delEnt"),
    url(r'^modifier/(?P<pk>\d+)$',"entreprise.views.modifEnt",name="modifEnt"),

)
