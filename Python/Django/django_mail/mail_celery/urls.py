from django.urls import path
from .views import HomeCreateView, add_to_database, send_message

urlpatterns = [
    path("", HomeCreateView.as_view(), name="home"),
    path("data/", add_to_database),
    path("send/", send_message)
]
