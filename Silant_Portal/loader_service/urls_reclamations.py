from django.urls import path

from .views import ReclamationView, ReclamationDetail, ReclamationCreate


urlpatterns = [
    path('', ReclamationView.as_view(), name='reclamations'),
    path('create', ReclamationCreate.as_view(), name='reclamations_create'),
    path('<int:pk>', ReclamationDetail.as_view(), name='reclamations_detail'),
]
