from django.urls import path

from .views import landingPage, registerPage, loginPage, logoutPage, homePage


app_name = 'streakchat'

urlpatterns = [
    path(route='', view=landingPage, name='landingPage'),
    path(route='register', view=registerPage, name='registerPage'),
    path(route='login', view=loginPage, name='loginPage'),
    path(route='logout', view=logoutPage, name='logoutPage'),
    path(route='home', view=homePage, name='homePage')
]   