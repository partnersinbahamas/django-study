from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_main, name="news-home"),
    path('add/', views.add_form, name="news-add")
]