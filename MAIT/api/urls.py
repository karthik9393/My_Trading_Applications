from django.urls import path
from . import views

urlpatterns = [
    path('', view = views.getRoutes),
    path('notes/', views.getNotes)
]