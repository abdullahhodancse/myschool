from django.urls import path
from app1.views import subscription

urlpatterns = [
    path("no/", subscription, name="sub"),
]
