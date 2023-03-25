
from django.urls import path
from . import views

app_name = 'clubfeed'

urlpatterns = [
    path('addPost/', views.addPost , name='addPost'),
    path('like/<int:post_id>/', views.like, name='like'),
]
