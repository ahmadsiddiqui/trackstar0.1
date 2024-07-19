from django.urls import include, path

from . import views

urlpatterns = [
	path("", views.index, name = "index"),
	path("signup", views.signup, name ="signup"),
	path("login", views.login, name="login")
	]
