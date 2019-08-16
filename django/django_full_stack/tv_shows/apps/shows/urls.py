from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.shows_all),
    url(r'^shows/(?P<shows_id>\d+)/edit$', views.shows_edit),
    url(r'^shows/(?P<shows_id>\d+)$', views.shows_view),
    url(r'^shows/new$', views.shows_new),

    
]