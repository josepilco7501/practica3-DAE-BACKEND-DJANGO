from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('postulantes',views.PostulanteView.as_view(),name='postulantes'),
    path('postulante/<int:postulantes_id>',views.PostulanteDetailView.as_view())
]
