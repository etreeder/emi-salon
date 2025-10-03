from django.urls import path
from . import views

app_name = "salon"
urlpatterns = [
    path("", views.Index.as_view(), name="home"),
    path("gallery", views.Gallery.as_view(), name="gallery"),
    path("create", views.Image.as_view(), name="imagecreate"),
    # image detail
    # services
    # contact
    # profile
    # book
    # 
]