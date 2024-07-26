from django.urls import path

from .views import ProfileView, ProfileDelete, ProfileUpdateView, EquipmentModelView


urlpatterns = [
    path('profiles/', ProfileView.as_view(), name='profiles'),
    path('profiles/<int:pk>/delete/', ProfileDelete.as_view(), name='profile_delete'),
    path('profiles/<int:pk>/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('equipment_models', EquipmentModelView.as_view(), name='equipment_models'),
]
