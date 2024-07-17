from django_filters import FilterSet, ChoiceFilter

from .models import Machine, Reclamation, TechService


class MachineFilter(FilterSet):
    class Meta:
        model = Machine
        fields = {
            'equipment_model': ['icontains'],
            'engine_model': ['icontains'],
            'transmission_model': ['icontains'],
            'driving_axle_model': ['icontains'],
            'control_axle_model': ['icontains'],
        }


class TechServiceFilter(FilterSet):
    class Meta:
        model = TechService
        fields = {
            'service_type': ['icontains'],
            'machine__equipment_model': ['icontains'],
            'service_company': ['icontains'],
        }


class ReclamationFilter(FilterSet):
    class Meta:
        model = Reclamation
        fields = {
            'workoff_node': ['icontains'],
            'repair_method': ['icontains'],
            'service_company': ['icontains'],
        }
