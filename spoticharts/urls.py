from django.urls import path
from . import views
app_name = 'spoticharts'
urlpatterns = [
    path('', views.index, name='index'),
]