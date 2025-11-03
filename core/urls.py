from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ← Maps the root URL to your home view
]