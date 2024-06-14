from django.urls import path
from . import views

urlpatterns = [
  path("", views.page_index),
  path("dashboard", views.page_beranda),
  path("status", views.page_status)

]
