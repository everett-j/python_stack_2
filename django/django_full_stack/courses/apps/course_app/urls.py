from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    #url(r'^shows$', views.shows_all),
    #url(r'^update_show/(?P<shows_id>\d+)$', views.shows_edit_me),


    
]