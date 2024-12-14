from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_main, name="news-home"),
    path('add/', views.add_form, name="news-add"),
    # <int:pk> means that we will have dynamic link param
    # if we use class view, we need to use as_view method
    path('<int:pk>', views.NewsDetailView.as_view(), name="news-details")
]