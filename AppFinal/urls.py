from django.urls import path, include
from AppFinal import views
from django.contrib.auth.views import LogoutView


app_name="AppFinal"

urlpatterns = [
    path("", views.inicio, name="inicio"),
     path("americanasAle", views.americanasAle, name="americanasAle"),
     path ("alemanasChecasAustriacasAle", views.alemanasChecasAustriacasAle, name="alemanasChecasAustriacasAle"),
     path ("belgasFrancesasAle", views.belgasFrancesasAle, name= "belgasFrancesasAle"),
     path ("britanicasAle", views.britanicasAle, name="britanicasAle"),
     path ("internacionalesAle", views.internacionalesAle, name="internacionalesAle"),
     path ("americanasLager", views.americanasLager, name="americanasLager"),
     path ("alemanasChecasAustriacasLager", views.alemanasChecasAustriacasLager, name="alemanasChecasAustriacasLager"),
     path ("internacionalesLager", views.internacionalesLager, name="internacionalesLager"),
     path ("otras", views.otras, name="otras"),
     path ("cargarReceta", views.cargarReceta, name="cargarReceta"),
     path ("mostrar", views.mostrarReceta, name="mostrarReceta"),
     path ("leerAmericanasAle", views.leerAmericanasAle, name="leerAmericanasAle"),
     path ("leerAlemanasChecasAustriacasAle", views.leerAlemanasChecasAustriacasAle, name="leerAlemanasChecasAustriacasAle"),
     path ("leerBelgasFrancesasAle", views.leerBelgasFrancesasAle, name="leerBelgasFrancesasAle"),
     path("leerBritanicasAle", views.leerBritanicasAle, name="leerBritanicasAle"),
     path("leerInternacionalesAle", views.leerInternacionalesAle, name="leerInternacionalesAle"),
     path("leerAmericanasLager", views.leerAmericanasLager, name="leerAmericanasLager"),
     path("leerAlemanasChecasAustriacasLager", views.leerAlemanasChecasAustriacasLager, name="leerAlemanasChecasAustriacasLager"),
     path("leerInternacionalesLager", views.leerInternacionalesLager, name="leerInternacionalesLager"),
     path("leerOtras", views.leerOtras, name="leerOtras"),
     path ("editarAmericanasAle", views.editarAmericanasAle, name="editarAmericanasAle"),
     path ("editarAlemanasChecasAustriacasAle", views.editarAlemanasChecasAustriacasAle, name="editarAlemanasChecasAustriacasAle"),
     path ("editarBelgasFrancesasAle", views.editarBelgasFrancesasAle, name="editarBelgasFrancesasAle"),
     path ("editarBritanicasAle", views.editarBritanicasAle, name="editarBritanicasAle"),
     path ("editarInternacionalesAle", views.editarInternacionalesAle, name="editarInternacionalesAle"),
     path ("editarAmericanasLager", views.editarAmericanasLager, name="editarAmericanasLager"),
     path ("editarAlemanasChecasAustriacasLager", views.editarAlemanasChecasAustriacasLager, name="editarAlemanasChecasAustriacasLager"),
     path ("editarInternacionalesLager", views.editarInternacionalesLager, name="editarInternacionalesLager"),
     path ("editarOtras", views.editarOtras, name="editarOtras"),
     path ("eliminarAmericanasAle/<americanasAle_nombre>/", views.eliminarAmericanasAle, name="eliminarAmericanasAle"),
     path ("eliminarAlemanasChecasAustriacasAle/<alemanasChecasAustriacasAle_nombre>/", views.eliminarAlemanasChecasAustriacasAle, name="eliminarAlemanasChecasAustriacasAle"),
     path ("eliminarBelgasFrancesasAle/<belgasFrancesasAle_nombre>/", views.eliminarBelgasFrancesasAle, name="eliminarBelgasFrancesasAle"),
     path ("eliminarBritanicasAle/<britanicasAle_nombre>/", views.eliminarBritanicasAle, name="eliminarBritanicasAle"),
     path ("eliminarInternacionalesAle/<internacionalesAle_nombre>/", views.eliminarInternacionalesAle, name="eliminarInternacionalesAle"),
     path ("eliminarAmericanasLager/<americanasLager_nombre>/", views.eliminarAmericanasLager, name="eliminarAmericanasLager"),
     path ("eliminarAlemanasChecasAustriacasLager/<alemanasChecasAustriacasLager_nombre>/", views.eliminarAlemanasChecasAustriacasLager, name="eliminarAlemanasChecasAustriacasLager"),
     path ("eliminarInternacionalesLager/<internacionalesLager_nombre>/", views.eliminarInternacionalesLager, name="eliminarInternacionalesLager"),
     path ("eliminarOtras/<otras_nombre>/", views.eliminarOtras, name="eliminarOtras"),



    #path ("americanasLager/list", views.AmericanasLagerList.as_view(), name= "list"),
    #path ("americanasLager/<int:pk>", views.AmericanasLagerDetalle.as_view(), name= "detail"),
    #path("nuevo", views.AmericanasLagerCreacion.as_view(), name ="new"),
    #path("editar/<int:pk>", views.AmericanasLagerUpdate.as_view(), name ="edit"),
    #path("borrar/<int:pk>", views.AmericanasLagerDelete.as_view(), name ="delete"),

    #path("americanasAle/list", views.AmericanasAleList.as_view(), name="list"),
    #path ("<int:pk>", views.AmericanasAleDetalle.as_view(), name= "detail"),
    #path("nuevo", views.AmericanasAleCreacion.as_view(), name ="new"),
    #path("editar/<int:pk>", views.AmericanasAleUpdate.as_view(), name ="edit"),
    #path("borrar/<int:pk>", views.AmericanasAleDelete.as_view(), name ="delete"),

]