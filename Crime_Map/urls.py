from django.urls import path
from . import views

app_name = "Crime_Map"

urlpatterns = [
    path("", views.index, name="index"),
    path("raw_data", views.raw_data, name="raw_data"),
    path("data_csv", views.data_csv, name="data_csv"),
    path("current_csv", views.current_csv, name="current_csv")
]

