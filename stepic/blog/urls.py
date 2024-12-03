from django.urls import path, re_path, include
from blog import views

product_patterns = [
    path("", views.products),
    path("new/", views.new),
    path("top/", views.top),

]


urlpatterns = [
               path("", views.index),
               path("products/<int:id>/", include(product_patterns)),
                             
               ]