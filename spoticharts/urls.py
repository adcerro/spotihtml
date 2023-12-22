from django.urls import path
from . import views
app_name = 'spoticharts'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('charts', views.charts, name='charts'),
]