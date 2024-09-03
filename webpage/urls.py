from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexPage, name="index"),
    path("about/", views.aboutPage, name="about"),
    path("contact/", views.contactPage, name='contact'),
    path("login/", views.loginPage, name='login'),
    path("register/", views.registerPage, name='register'),

]