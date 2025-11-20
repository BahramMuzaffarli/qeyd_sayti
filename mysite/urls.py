from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login_page, name="login"),       # əsas səhifə login
    path("index/", views.index, name="index"),      # Salam Bahram səhifəsi
    path("welcome/", views.welcome, name="welcome"),  # welcome səhifəsi
    path("notes/", views.notes_list, name="notes_list"), # New notes list page
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("note/<int:id>/edit/", views.edit_note, name="edit_note"),
    path("note/create/", views.create_note, name="create_note"),
    path("lang/<str:lang>/", views.change_language, name="change_language"),
    path("note/<int:id>/delete/", views.delete_note, name="delete_note"),
    path("users/", views.users_list, name="users_list"),
    path("users/create/", views.create_user, name="create_user"),
    path("users/<int:id>/edit/", views.edit_user, name="edit_user"),
    path("users/<int:id>/delete/", views.delete_user, name="delete_user"),
    path("menu/", views.menu_page, name="menu_page"),
    path("menu/upload/", views.upload_media, name="upload_media"),
    path("menu/<int:id>/delete/", views.delete_media, name="delete_media"),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
