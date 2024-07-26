import django_filters
from django_filters import FilterSet, ChoiceFilter

from .models import Machine, Reclamation, TechService, Profile, EquipmentModel


class ProfileFilter(FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Profile
        fields = {
            'username': ['icontains']
        }


class MachineFilter(FilterSet):
    equipment_number = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Machine
        fields = {
            'equipment_number': ['contains'],
            'equipment_model': ['exact'],
            'engine_model': ['exact'],
            'transmission_model': ['exact'],
            'driving_axle_model': ['exact'],
            'control_axle_model': ['exact']
        }


class TechServiceFilter(FilterSet):
    class Meta:
        model = TechService
        fields = {
            'service_type': ['exact'],
            'machine__equipment_model': ['exact'],
            'service_company': ['exact'],
        }


class ReclamationFilter(FilterSet):
    repair_method = django_filters.CharFilter(lookup_expr='icontains')
    workoff_node = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Reclamation
        fields = {
            'workoff_node': ['contains'],
            'repair_method': ['contains'],
            'service_company': ['exact'],
        }


class EquipmentModelFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = EquipmentModel
        fields = {
            'title', 'description'
        }