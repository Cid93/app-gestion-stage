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
    url(r'^(?P<pk>\d+)$',"stage.views.show_detail_stage", name="stage"),
    url(r'^modifier/(?P<pk>\d+)$',"stage.views.modifStage", name="modifStage"),
    url(r'^monStage/?$',"stage.views.monStage", name="theStage"),
    url(r'^ajouter/?$',"stage.views.addStage", name="addStage"),
    url(r'^supprimer/?$',"stage.views.delStage", name="delStage"),
    url(r'^personne-ext/$',"stage.views.addPersonneExt",name="addPersonneExt"),
    url(r'^ok/?$',"stage.views.stage_operationEffectuee", name="stageOperationEffectuee"),
    url(r'^valider/?$',"stage.views.validerStage", name="validerStage"),
    url(r'^detailsvalider/(?P<pk>\d+)$',"stage.views.detailsValiderStage", name="detailsValiderStage"),
    url(r'^validerenbase/(?P<pk>\d+)$',"stage.views.validerStageEnBase", name="validerStageEnBase"),

    url(r'^offrestage/?$',"stage.views.showOffres", name="showOffres"),
    url(r'^offrestage/(?P<pk>\d+)$',"stage.views.detailsOffreStage", name="detailsOffreStage"),
    url(r'^offrestage/modifier/(?P<pk>\d+)$',"stage.views.modifOffreStage", name="modifOffreStage"),
    url(r'^offrestage/ajouter/?$',"stage.views.addOffreStage", name="addOffreStage"),
    url(r'^offrestage/supprimer/?$',"stage.views.delOffreStage", name="delOffreStage"),
    url(r'^offrestage/ok/?$',"stage.views.offreStage_operationEffectuee", name="offreStageOperationEffectuee"),
    url(r'^offrestage/valider/?$',"stage.views.validerOffreStage", name="validerOffreStage"),
    url(r'^offrestage/detailsvalider/(?P<pk>\d+)$',"stage.views.detailsValiderOffreStage", name="detailsValiderOffreStage"),
    url(r'^offrestage/validerenbase/(?P<pk>\d+)$',"stage.views.validerOffreStageEnBase", name="validerOffreStageEnBase"),
)