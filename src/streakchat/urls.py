from django.urls import path

from . import views


app_name = 'streakchat'

urlpatterns = [
    path(route='', view=views.index, name='index'),
]