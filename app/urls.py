from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("termsnserviece/", views.termsnserviece, name="termsnserviece"),
    path("privacypolicy/", views.privacypolicy, name="privacypolicy"),
    path("help/", views.help, name="help"),
    path("feedback/", views.feedback, name="feedback"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("base/", views.base, name="base"),
    # path("movie/<int:movie_id>", views.movie_detail, name="movie_detail"),
]
