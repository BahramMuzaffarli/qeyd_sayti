from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login_page, name="login"),       # əsas səhifə login
    path("index/", views.index, name="index"),      # Salam Bahram səhifəsi
    path("welcome/", views.welcome, name="welcome"),  # welcome səhifəsi
    path("logout/", views.logout_view, name="logout"),
    path("note/<int:id>/edit/", views.edit_note, name="edit_note"),
    path("note/create/", views.create_note, name="create_note"),
    path("lang/<str:lang>/", views.change_language, name="change_language"),
    path("note/<int:id>/delete/", views.delete_note, name="delete_note"),
    path("users/", views.users_list, name="users_list"),
    path("users/create/", views.create_user, name="create_user"),
    path("users/<int:id>/edit/", views.edit_user, name="edit_user"),
    path("users/<int:id>/delete/", views.delete_user, name="delete_user"),


]
