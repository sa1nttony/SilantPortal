from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import (
    Machine,
    TechService,
    Reclamation,
    Profile,
    TransmissionModel,
    EquipmentModel,
    EngineModel,
    DrivingAxleModel,
    ControlAxleModel,
    ServiceType,
    ServiceCompany,
    RepairMethod,
    WorkoffNode
)
from .filters import (
    MachineFilter,
    TechServiceFilter,
    ReclamationFilter,
    ProfileFilter,
    EquipmentModelFilter,
    EngineModelFilter,
    TransmissionModelFilter,
    DrivingAxleModelFilter,
    ControlAxleModelFilter,
    ServiceTypeFilter,
    ServiceCompanyFilter,
    WorkoffNodeFilter,
    RepairMethodFilter
)
from .forms import (
    MachineForm,
    AddUserForm,
    UpdateUserForm,
    TechServiceForm,
    ReclamationForm,
    EquipmentModelForm,
    EngineModelForm,
    TransmissionModelForm,
    DrivingAxleModelForm,
    ControlAxleModelForm,
    ServiceTypeForm,
    ServiceCompanyForm,
    RepairMethodForm,
    WorkoffNodeForm
)

# Create your views here.


#Profile----------------------------
class AddUserView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = AddUserForm
    success_url = '/administration/profiles/'
    template_name = 'registration/add_user.html'


class ProfileView(LoginRequiredMixin, ListView):
    raise_exception = True
    model = Profile
    ordering = "username"
    template_name = 'profiles.html'
    context_object_name = 'profiles'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProfileFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filterset'] = self.filterset
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    raise_exception = True
    model = Profile
    form_class = UpdateUserForm
    template_name = "profile_update.html"
    success_url = reverse_lazy('profiles')


class ProfileDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Profile
    template_name = 'profile_delete.html'
    success_url = reverse_lazy('profiles')


#Machine----------------------------
class MachineView(ListView):
    model = Machine
    ordering = 'shipment_out_date'
    template_name = 'home.html'
    context_object_name = 'machines'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = MachineFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filterset'] = self.filterset
        return context


class MachineDetailView(LoginRequiredMixin, DetailView):
    raise_exception = True
    model = Machine
    context_object_name = 'machine_detail'
    template_name = 'machines_detail.html'
    queryset = Machine.objects.all()


class MachineCreateView(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = Machine
    form_class = MachineForm
    template_name = 'machine_create.html'
    success_url = reverse_lazy('machines_list')


class MachineUpdateView(LoginRequiredMixin, UpdateView):
    raise_exception = True
    model = Machine
    form_class = MachineForm
    template_name = 'machines_update.html'
    success_url = reverse_lazy('machines_list')


class MachineDeleteView(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Machine
    template_name = 'machines_delete.html'
    success_url = reverse_lazy('machines_list')


#TO----------------------------
class TechServiceView(LoginRequiredMixin, ListView):
    raise_exception = True
    model = TechService
    ordering = 'service_date'
    template_name = 'techservices.html'
    context_object_name = 'tech_services'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = TechServiceFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filterset'] = self.filterset
        return context


class TechServiceDetail(LoginRequiredMixin, DetailView):
    raise_exception = True
    model = TechService
    context_object_name = 'tech_service_detail'
    template_name = 'tech_service_detail.html'
    queryset = TechService.objects.all()


class TechServiceCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = TechServiceForm
    template_name = 'tech_service_create.html'
    success_url = reverse_lazy('tech_services')


class TechServiceUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    model = TechService
    form_class = TechServiceForm
    template_name = 'tech_service_update.html'
    success_url = reverse_lazy('tech_services')


class TechServiceDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = TechService
    template_name = 'tech_service_delete.htm'
    success_url = reverse_lazy('tech_services')


#Reclamation----------------------------
class ReclamationView(LoginRequiredMixin, ListView):
    raise_exception = True
    model = Reclamation
    ordering = 'workoff_date'
    template_name = 'reclamations.html'
    context_object_name = 'reclamations'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ReclamationFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filterset'] = self.filterset
        return context


class ReclamationDetail(DetailView):
    raise_exception = True
    model = Reclamation
    context_object_name = 'reclamation_detail'
    template_name = 'reclamation_detail.html'
    queryset = Reclamation.objects.all()


class ReclamationCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = Reclamation
    form_class = ReclamationForm
    template_name = 'reclamation_create.html'
    success_url = reverse_lazy('reclamations')


class ReclamationUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    model = Reclamation
    form_class = ReclamationForm
    template_name = 'reclamation_update.html'
    success_url = reverse_lazy('reclamations')


class ReclamationDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Reclamation
    template_name = 'reclamation_delete.html'
    success_url = reverse_lazy('reclamations')


#Справочники------------------
#Модель техники
class EquipmentModelView(ListView):
    model = EquipmentModel
    ordering = 'title'
    template_name = 'equipment_models.html'
    context_object_name = 'equipment_models'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = EquipmentModelFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filterset'] = self.filterset
        return context


class EquipmentModelDetail(DetailView):
    model = EquipmentModel
    context_object_name = 'equipment_model_detail'
    template_name = 'equipment_model_detail.html'
    queryset = EquipmentModel.objects.all()


class EquipmentModelCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = EquipmentModel
    template_name = 'equipment_model_create.html'
    form_class = EquipmentModelForm
    success_url = reverse_lazy('equipment_models')


class EquipmentModelDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = EquipmentModel
    template_name = 'equipment_model_delete.html'
    success_url = reverse_lazy('equipment_models')


class EquipmentModelUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = EquipmentModelForm
    model = EquipmentModel
    template_name = 'equipment_model_update.html'
    success_url = reverse_lazy('equipment_models')


#Модель двигателя
class EngineModelView(ListView):
    model = EngineModel
    ordering = 'title'
    template_name = 'engine_models.html'
    context_object_name = 'engine_models'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = EngineModelFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filterset'] = self.filterset
        return context


class EngineModelDetail(DetailView):
    model = EngineModel
    context_object_name = 'engine_model_detail'
    template_name = 'engine_model_detail.html'
    queryset = EngineModel.objects.all()


class EngineModelCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = EngineModel
    template_name = 'engine_model_create.html'
    form_class = EngineModelForm
    success_url = reverse_lazy('engine_models')


class EngineModelDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = EngineModel
    template_name = 'engine_model_delete.html'
    success_url = reverse_lazy('engine_models')


class EngineModelUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = EngineModelForm
    model = EngineModel
    template_name = 'engine_model_update.html'
    success_url = reverse_lazy('engine_models')


#Модель трансмиссии
class TransmissionModelView(ListView):
    model = TransmissionModel
    ordering = 'title'
    template_name = 'transmission_models.html'
    context_object_name = 'transmission_models'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = TransmissionModelFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filterset'] = self.filterset
        return context


class TransmissionModelDetail(DetailView):
    model = TransmissionModel
    context_object_name = 'transmission_model_detail'
    template_name = 'transmission_model_detail.html'
    queryset = TransmissionModel.objects.all()


class TransmissionModelCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = TransmissionModel
    template_name = 'transmission_model_create.html'
    form_class = TransmissionModelForm
    success_url = reverse_lazy('transmission_models')


class TransmissionModelDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = TransmissionModel
    template_name = 'transmission_model_delete.html'
    success_url = reverse_lazy('transmission_models')


class TransmissionModelUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = TransmissionModelForm
    model = TransmissionModel
    template_name = 'transmission_model_update.html'
    success_url = reverse_lazy('transmission_models')


#Модель ведущего моста
class DrivingAxleModelView(ListView):
    model = DrivingAxleModel
    ordering = 'title'
    template_name = 'driving_axle_models.html'
    context_object_name = 'driving_axle_models'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = DrivingAxleModelFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filterset'] = self.filterset
        return context


class DrivingAxleModelDetail(DetailView):
    model = DrivingAxleModel
    context_object_name = 'driving_axle_model_detail'
    template_name = 'driving_axle_model_detail.html'
    queryset = DrivingAxleModel.objects.all()


class DrivingAxleModelCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = DrivingAxleModel
    template_name = 'driving_axle_model_create.html'
    form_class = DrivingAxleModelForm
    success_url = reverse_lazy('driving_axle_models')


class DrivingAxleModelDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = DrivingAxleModel
    template_name = 'driving_axle_model_delete.html'
    success_url = reverse_lazy('driving_axle_models')


class DrivingAxleModelUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = DrivingAxleModelForm
    model = DrivingAxleModel
    template_name = 'driving_axle_model_update.html'
    success_url = reverse_lazy('driving_axle_models')


#Модель управляемого моста
class ControlAxleModelView(ListView):
    model = ControlAxleModel
    ordering = 'title'
    template_name = 'control_axle_models.html'
    context_object_name = 'control_axle_models'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ControlAxleModelFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filterset'] = self.filterset
        return context


class ControlAxleModelDetail(DetailView):
    model = ControlAxleModel
    context_object_name = 'control_axle_model_detail'
    template_name = 'control_axle_model_detail.html'
    queryset = ControlAxleModel.objects.all()


class ControlAxleModelCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = ControlAxleModel
    template_name = 'control_axle_model_create.html'
    form_class = ControlAxleModelForm
    success_url = reverse_lazy('control_axle_models')


class ControlAxleModelDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = ControlAxleModel
    template_name = 'control_axle_model_delete.html'
    success_url = reverse_lazy('control_axle_models')


class ControlAxleModelUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = ControlAxleModelForm
    model = ControlAxleModel
    template_name = 'control_axle_model_update.html'
    success_url = reverse_lazy('control_axle_models')


#Модель управляемого моста
class ServiceTypeView(ListView):
    model = ServiceType
    ordering = 'title'
    template_name = 'service_types.html'
    context_object_name = 'service_types'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ServiceTypeFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filterset'] = self.filterset
        return context


class ServiceTypeDetail(DetailView):
    model = ServiceType
    context_object_name = 'service_type_detail'
    template_name = 'service_type_detail.html'
    queryset = ServiceType.objects.all()


class ServiceTypeCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = ServiceType
    template_name = 'service_type_create.html'
    form_class = ServiceTypeForm
    success_url = reverse_lazy('service_types')


class ServiceTypeDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = ServiceType
    template_name = 'service_type_delete.html'
    success_url = reverse_lazy('service_types')


class ServiceTypeUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = ServiceTypeForm
    model = ServiceType
    template_name = 'service_type_update.html'
    success_url = reverse_lazy('service_types')


#Модель управляемого моста
class ServiceCompanyView(ListView):
    model = ServiceCompany
    ordering = 'title'
    template_name = 'service_companies.html'
    context_object_name = 'service_companies'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ServiceCompanyFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filterset'] = self.filterset
        return context


class ServiceCompanyDetail(DetailView):
    model = ServiceType
    context_object_name = 'service_company_detail'
    template_name = 'service_company_detail.html'
    queryset = ServiceCompany.objects.all()


class ServiceCompanyCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = ServiceCompany
    template_name = 'service_company_create.html'
    form_class = ServiceCompanyForm
    success_url = reverse_lazy('service_companies')


class ServiceCompanyDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = ServiceCompany
    template_name = 'service_company_delete.html'
    success_url = reverse_lazy('service_companies')


class ServiceCompanyUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = ServiceCompanyForm
    model = ServiceCompany
    template_name = 'service_company_update.html'
    success_url = reverse_lazy('service_companies')


#Метод восстановления
class RepairMethodView(ListView):
    model = RepairMethod
    ordering = 'title'
    template_name = 'repair_methods.html'
    context_object_name = 'repair_methods'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = RepairMethodFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filterset'] = self.filterset
        return context


class RepairMethodDetail(DetailView):
    model = RepairMethod
    context_object_name = 'repair_method_detail'
    template_name = 'repair_method_detail.html'
    queryset = RepairMethod.objects.all()


class RepairMethodCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = RepairMethod
    template_name = 'repair_method_create.html'
    form_class = RepairMethodForm
    success_url = reverse_lazy('repair_methods')


class RepairMethodDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = RepairMethod
    template_name = 'repair_method_delete.html'
    success_url = reverse_lazy('repair_methods')


class RepairMethodUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = RepairMethodForm
    model = RepairMethod
    template_name = 'repair_method_update.html'
    success_url = reverse_lazy('repair_methods')


#Узел отказа
class WorkoffNodeView(ListView):
    model = WorkoffNode
    ordering = 'title'
    template_name = 'workoff_nodes.html'
    context_object_name = 'workoff_nodes'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = WorkoffNodeFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filterset'] = self.filterset
        return context


class WorkoffNodeDetail(DetailView):
    model = WorkoffNode
    context_object_name = 'workoff_node_detail'
    template_name = 'workoff_node_detail.html'
    queryset = WorkoffNode.objects.all()


class WorkoffNodeCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = WorkoffNode
    template_name = 'workoff_node_create.html'
    form_class = WorkoffNodeForm
    success_url = reverse_lazy('workoff_nodes')


class WorkoffNodeDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = WorkoffNode
    template_name = 'workoff_node_delete.html'
    success_url = reverse_lazy('workoff_nodes')


class WorkoffNodeUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = WorkoffNodeForm
    model = WorkoffNode
    template_name = 'workoff_node_update.html'
    success_url = reverse_lazy('workoff_nodes')
