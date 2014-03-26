from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   
	# Planning
    url(r'^$', "planning.views.show_planning", name="show_planning"),
    url(r'^(?P<pk>\d+)$', "planning.views.show_soutenance", name="show_soutenance"),
    url(r'^find/$', "planning.views.find_planning", name="find_planning"),

    url(r'^ajout/$', "planning.views.addSoutenance", name="addSoutenance"),
    url(r'^ajouterSalle/$', "planning.views.addSalle", name="addSalle"),

    url(r'^modifier/(?P<pk>\d+)$', "planning.views.editSoutenance", name="editSoutenance"),
)
