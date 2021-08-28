from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.id_person_update.as_view(), name='id_person'),
]
