from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # We’ll make the 'home' view next
]
