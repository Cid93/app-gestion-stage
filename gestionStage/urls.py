from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # racine et page par defaut, pages classiques
    url(r'^/?$',"gestionStage.views.show_main", name="accueil"),
    url(r'^login/$', "gestionStage.forms.login_page", name="login"),
    url(r'^logout/$', "gestionStage.forms.logout_action", name="logout"),
    url(r'^oups/$',"gestionStage.views.oups",name="oups"),
    url(r'^recherche/$',"gestionStage.views.search",name="search"),

    # app entreprise
    url(r'^entreprise/', include('entreprise.urls')),
    url(r'^visiter/$', "entreprise.views.show_visiter", name="visiter"),

    # app stage
    url(r'^stage/', include('stage.urls')),

    # app planning
    url(r'^planning/', include('planning.urls')),


    url(r'^monProfilEtudiant/?$',"stage.views.monProfilEtu", name="monProfil"),
    url(r'^etudiant/(?P<pk>\d+)$',"stage.views.detailsEtudiant", name="detailsEtudiant"),
    url(r'^etudiant/modifier/(?P<pk>\d+)$',"stage.views.modifEtudiant", name="modifEtudiant"),

    url(r'^monProfilEnseignant/?$',"stage.views.monProfilEns", name="monProfil"),
    url(r'^enseignant/(?P<pk>\d+)$',"stage.views.detailsEnseignant", name="detailsEnseignant"),
    url(r'^enseignant/modifier/(?P<pk>\d+)$',"stage.views.modifEnseignant", name="modifEnseignant"),

    url(r'^findData/?$', "gestionStage.views.find_data", name="find_data")


)
