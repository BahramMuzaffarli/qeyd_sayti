from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login_page, name="login"),       # əsas səhifə login
    path("index/", views.index, name="index"),      # Salam Bahram səhifəsi
    path("welcome/", views.welcome, name="welcome"),  # welcome səhifəsi
    path("logout/", views.logout_view, name="logout"),

]
