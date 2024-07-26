from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Profile, Machine, TechService, Reclamation, EquipmentModel, EngineModel, TransmissionModel, DrivingAxleModel, ControlAxleModel, ServiceType, ServiceCompany


class AddUserForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password1', 'password2', 'role', 'bio']


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'role', 'bio']


class DateInput(forms.DateInput):
    input_type = 'date'


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = [
            'equipment_number',
            'equipment_model',
            'engine_model',
            'engine_number',
            'transmission_model',
            'transmission_number',
            'driving_axle_model',
            'driving_axle_number',
            'control_axle_model',
            'control_axle_number',
            'shipment_contract',
            'shipment_out_date',
            'consignee',
            'shipment_adress',
            'options',
            'client',
            'service_company',
        ]
        widgets = {'shipment_out_date': DateInput()}


class TechServiceForm(forms.ModelForm):
    class Meta:
        model = TechService
        fields = [
            'service_type',
            'service_date',
            'mileage',
            'order_number',
            'order_date',
            'machine',
            'service_company',
        ]

        widgets = {'service_date': DateTimeInput(), 'order_date': DateInput(),}


class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = [
            'workoff_date',
            'mileage',
            'workoff_node',
            'workoff_descriprion',
            'repair_method',
            'used_recovery_kit',
            'repair_date',
            'dead_time',
            'machine',
            'service_company',
        ]


class EquipmentModelForm(forms.ModelForm):
    class Meta:
        model = EquipmentModel
        fields = ['title', 'description']


class EngineModelForm(forms.ModelForm):
    class Meta:
        model = EngineModel
        fields = ['title', 'description']


class TransmissionModelForm(forms.ModelForm):
    class Meta:
        model = TransmissionModel
        fields = ['title', 'description']


class DrivingAxleModelForm(forms.ModelForm):
    class Meta:
        model = DrivingAxleModel
        fields = ['title', 'description']


class ControlAxleModelForm(forms.ModelForm):
    class Meta:
        model = ControlAxleModel
        fields = ['title', 'description']


class ServiceTypeForm(forms.ModelForm):
    class Meta:
        model = ServiceType
        fields = ['title', 'description']


class ServiceCompanyForm(forms.ModelForm):
    class Meta:
        model = ServiceCompany
        fields = ['title', 'description', 'profile']
