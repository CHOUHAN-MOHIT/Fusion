
from django.urls import path
from . import views

app_name = 'clubfeed'

urlpatterns = [
    path('addPost/', views.addPost , name='addPost'),
    path('like/<int:post_id>/', views.like, name='like'),
    # path('posts/<int:post_id>/', views.show_comment, name='show_comment'),
    path('addcomment/<int:post_id>/', views.add_comment, name='addcomment')
]
