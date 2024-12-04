from django.urls import path, re_path, include
from blog import views

urlpatterns = [
               path("index/<int:id>/", views.index),
               path("access/<int:age>/", views.access),

                             
               ]