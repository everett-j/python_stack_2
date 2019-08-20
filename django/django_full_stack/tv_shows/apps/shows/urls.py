from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.shows_all),
    url(r'^update_show/(?P<shows_id>\d+)$', views.shows_edit_me),
    url(r'^shows/(?P<shows_id>\d+)/edit$', views.shows_edit),
    url(r'^delete/(?P<shows_id>\d+)$', views.shows_delete),
    url(r'^shows/(?P<shows_id>\d+)$', views.shows_view),
    url(r'^shows/new$', views.shows_new),
    url(r'^new$', views.shows_newbie),
    url(r'^checkout$', views.checkout),
    url(r'^receipt$', views.receipt),
    url(r'^login$', views.loginregister),
    url(r'^register$', views.register),
    url(r'^logme', views.login),
    url(r'^success', views.success),
    url(r'^denied', views.denied),
    url(r'^logout', views.logout),

    
]