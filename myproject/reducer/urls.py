from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('reduced/', views.reduced, name='reduced'),
    path('S/<key>', views.get_link, name='get_link'),
]
