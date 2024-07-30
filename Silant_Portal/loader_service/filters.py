import django_filters
from django_filters import FilterSet, ChoiceFilter

from .models import (
    Machine,
    Reclamation,
    TechService,
    Profile,
    EquipmentModel,
    EngineModel,
    TransmissionModel,
    DrivingAxleModel,
    ControlAxleModel,
    ServiceType,
    ServiceCompany,
    WorkoffNode,
    RepairMethod
)


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
    class Meta:
        model = Reclamation
        fields = {
            'workoff_node': ['exact'],
            'repair_method': ['exact'],
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


class EngineModelFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = EngineModel
        fields = {
            'title', 'description'
        }


class TransmissionModelFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = TransmissionModel
        fields = {
            'title', 'description'
        }


class DrivingAxleModelFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = DrivingAxleModel
        fields = {
            'title', 'description'
        }


class ControlAxleModelFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = ControlAxleModel
        fields = {
            'title', 'description'
        }


class ServiceTypeFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = ServiceType
        fields = {
            'title', 'description'
        }


class ServiceCompanyFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = ServiceCompany
        fields = {
            'title', 'description', 'profile'
        }


class WorkoffNodeFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = WorkoffNode
        fields = {
            'title', 'description'
        }


class RepairMethodFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = RepairMethod
        fields = {
            'title', 'description'
        }