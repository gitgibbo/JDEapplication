"""Defines Patterns for BOS urls"""
from django.urls import path
from . import views

app_name = 'bos'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    #Page that shows BOS's
    path('boslist/', views.boslist, name='boslist'),
    # Detail page for a single BOS
    path('bos/<int:bos_id>/',views.bos, name='bos'),
    # BOS entry
    path('newbos/', views.newbos, name='newbos'),

]