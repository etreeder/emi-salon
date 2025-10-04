from django.urls import path
from . import views

app_name = "salon"
urlpatterns = [
    path("", views.Index.as_view(), name="home"),
    path("gallery", views.Gallery.as_view(), name="gallery"),
    path("create", views.ImageCreate.as_view(), name="image-new"),
    path("services", views.Services.as_view(), name="services"),
    path("services/create", views.ServiceCreate.as_view(), name="service-create"),
    path("services/<int:pk>", views.ServiceDetail.as_view(), name="service-detail"),    
    path("services/<int:pk>/update", views.ServiceUpdate.as_view(), name="service-update"),
    path("services/<int:pk>/delete", views.ServiceDelete.as_view(), name="service-delete"),
    # image detail
    # contact
    # profile
    # book
    # 
]