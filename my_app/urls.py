from django.urls import path, include
from . import views
from .views import new_search
from django.views.generic import TemplateView
urlpatterns = [
    path('home', views.home, name="home"),
    path('', TemplateView.as_view(template_name="base.html")),
    path('new_search', views.new_search, name="new_search"),
]
