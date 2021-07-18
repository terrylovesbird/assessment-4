  
from django.contrib import admin
from django.urls import path, include
from cj_app import views

app_name="cj"

urlpatterns = [
    path("", views.index, name="home"),
    path("categories", views.categories, name="category_list"), # a list of all the categories
    path("categories/new", views.category_new, name="category_new"), # form for a new category
    path("categories/<int:category_id>", views.category_detail, name="category_detail"), # see a specific category and its posts
    path("categories/<int:category_id>/edit", views.category_edit, name="category_edit"), # edit page for a specific category
    path("categories/<int:category_id>/delete", views.category_delete, name="category_delete"), # delete page for a specific category

    path("categories/<int:category_id>/posts", views.posts, name="post_list"), # a list of posts for a specific category
    path("categories/<int:category_id>/posts/new", views.post_new, name="post_new"), # form for a new post under a specific post category
    path("categories/<int:category_id>/posts/<int:post_id>", views.post_detail, name="post_detail"), # see a specific post for a specific post category, Also include the ability go back to the parent category detail page (/categories/:category_id/)
    path("categories/<int:category_id>/posts/<int:post_id>/edit", views.post_edit, name="post_edit"), # edit page for a specific post under a specific post category
    path("categories/<int:category_id>/posts/<int:post_id>/delete", views.post_delete, name="post_delete"), # delete page for a specific post under a specific post category
]