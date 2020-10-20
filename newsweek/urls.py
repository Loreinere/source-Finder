from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='newsweek-home'),
    path('about/', views.about, name='newsweek-about'),

]