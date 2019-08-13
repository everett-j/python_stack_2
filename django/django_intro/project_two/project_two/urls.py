from django.conf.urls import url, include	# added an import!
urlpatterns = [
    url(r'^', include('apps.app_two.urls')),	# use your app_name here
    ]
