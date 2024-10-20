from django.urls import path
from app.views import index, user

urlpatterns = [
    path('', index),
    path('user/', user)
]