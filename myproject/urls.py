from django.contrib import admin
from django.urls import include, path
from django.urls import path
from products import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("details/<int:id>", views.details),
    path("", views.index),
    path("create/", views.create),
    path("delete/<int:id>", views.delete),
    path("edit/<int:id>", views.edit),
    path('contact/',views.contact),
    path('main/',views.main),
    path('hotel/',views.hotel),
]
