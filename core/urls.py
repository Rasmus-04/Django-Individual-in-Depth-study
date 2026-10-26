from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("posts/", views.post_list, name="post_list"),
    path("posts/create/", views.post_create, name="post_create"),
    path("posts/<int:post_id>/edit/", views.post_update, name="post_update"),
    path("posts/<int:post_id>/delete/", views.post_delete, name="post_delete"),
]
