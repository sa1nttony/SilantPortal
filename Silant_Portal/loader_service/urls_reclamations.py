from django.urls import path

from .views import ReclamationView, ReclamationDetail, ReclamationCreate, ReclamationUpdate,ReclamationDelete


urlpatterns = [
    path('', ReclamationView.as_view(), name='reclamations'),
    path('create', ReclamationCreate.as_view(), name='reclamations_create'),
    path('<int:pk>', ReclamationDetail.as_view(), name='reclamations_detail'),
    path('<int:pk>/update', ReclamationUpdate.as_view(), name='reclamations_update'),
    path('<int:pk>/delete/', ReclamationUpdate.as_view(), name='reclamations_delete'),
]
