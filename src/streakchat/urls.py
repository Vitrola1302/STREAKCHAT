from django.urls import path

from . import views


app_name = 'streakchat'

urlpatterns = [
    path(route='', view=views.landingPage, name='landingPage'),
    path(route='register', view=views.registerPage, name='registerPage'),
    path(route='login', view=views.loginPage, name='loginPage'),
]   