from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subject/<int:subject_id>/', views.subject_detail, name='subject_detail'),
]