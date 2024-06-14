from django.urls import path
from . import views

urlpatterns = [
  path("", views.page_landing),
  path("about/", views.page_about),
  path("profil", views.page_profil),
  path("visi-misi", views.page_visi_misi),
  path("informasi", views.page_informasi),
  ]