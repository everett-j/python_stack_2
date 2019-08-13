from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninja2/calculateMoney$', views.calculateMoney),
    url(r'^ninja2/clear$', views.clear),
]