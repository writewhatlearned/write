from django.urls import path

from visit import views

app_name = 'visit'
urlpatterns = [
    path('', views.index, name='index')
]