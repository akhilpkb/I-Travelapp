from .import views
from django.urls import path

urlpatterns = [
    path('', views.hello,name='hello'),
    # path('about/', views.about,name='about'),
    # path('add/', views.addition, name='addtion'),
]
