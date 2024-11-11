from django.urls import path
from . import views
from django.conf.urls import handler404, handler500

handler404 = 'home.views.custom_404'
handler500 = 'home.views.custom_500'

urlpatterns = [
    path("", views.home, name="home"),
    path("contact", views.home, name="contact"),
    path("about", views.home, name="about"),
    path("features", views.home, name="features"),
    path("appointment", views.home, name="appointment"),
    path("learn_more", views.home, name="learn_more"),
    path("terms", views.terms, name="terms"),
    path("privacy", views.terms, name="privacy"),
    path("faq", views.faq, name="faq"),

]
