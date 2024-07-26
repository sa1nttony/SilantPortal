from django.urls import path

from .views import MachineView, MachineDetailView, MachineCreateView, MachineDeleteView, MachineUpdateView


urlpatterns = [
    path('', MachineView.as_view(), name='machines_list'),
    path('create', MachineCreateView.as_view(), name='machines_create'),
    path("<int:pk>", MachineDetailView.as_view(), name='machines_detail'),
    path("<int:pk>/delete", MachineDeleteView.as_view(), name='machines_delete'),
    path("<int:pk>/update", MachineUpdateView.as_view(), name='machines_update')
]
