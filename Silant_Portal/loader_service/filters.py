from django_filters import FilterSet, ChoiceFilter

from .models import Machine, Reclamation, TechService


class MachineFilter(FilterSet):
    class Meta:
        model = Machine
        fields = {
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
            'workoff_node': ['icontains'],
            'repair_method': ['icontains'],
            'service_company': ['exact'],
        }
