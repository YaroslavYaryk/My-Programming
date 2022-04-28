from django.urls import path
from .views import work_with_transaction


urlpatterns = [
    path("", work_with_transaction, name="home"),
]
