from django.conf.urls import include, url
from . import views

app_name = 'clubfeed'

urlpatterns = [
    url(r'^addPost/$', views.addPost , name='addPost'),
]
