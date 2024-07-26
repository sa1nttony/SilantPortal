from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Machine, TechService, Reclamation, Profile
from .filters import MachineFilter, TechServiceFilter, ReclamationFilter, ProfileFilter
from .forms import *

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
    model = Reclamation
    context_object_name = 'reclamation_detail'
    template_name = 'reclamation_detail.html'
    queryset = Reclamation.objects.all()