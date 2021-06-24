from django.urls import path

from . import views

urlpatterns = [
    path('enrol', views.enrol, name='enrol'),
]