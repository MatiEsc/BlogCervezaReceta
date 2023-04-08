from django.urls import path, include
from AppFinal import views
from django.contrib.auth.views import LogoutView


app_name="AppRegistro"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path ("login", views.login_request, name="login"),
    path ("register", views.register, name="register"),
    path ("logout", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path ("editarPerfil", views.editarPerfil,  name="editarPerfil"),
    path('agregarAvatar', views.agregarAvatar, name='AgregarAvatar'),

]