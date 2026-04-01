from django.urls import path
from . import views

urlpatterns = [
    path("", views.log_class, name="log"),
    path("history/", views.history, name="history"),
    path("stats/", views.stats, name="stats"),
]