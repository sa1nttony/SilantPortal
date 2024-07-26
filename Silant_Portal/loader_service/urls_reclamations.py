from django.urls import path

from .views import ReclamationView, ReclamationDetail


urlpatterns = [
    path('', ReclamationView.as_view(), name='reclamations'),
    path('<int:pk>', ReclamationDetail.as_view(), name='reclamations_detail'),
]
