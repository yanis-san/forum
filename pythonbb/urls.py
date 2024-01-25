from django.urls import path
from pythonbb.views import index

urlpatterns = [
    path("", index, name="index"),
]
