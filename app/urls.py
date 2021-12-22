from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.send, name='feedback'),
    path('stories/', views.story, name='stories'),
    path('gallery/', views.gallery, name='gallery'),
    path('work/', views.work, name='work'),
    path('donation/', views.donation, name='donation'),
    path('video/', views.video, name='video'),
]