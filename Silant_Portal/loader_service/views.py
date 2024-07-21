from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Machine, TechService, Reclamation
from .filters import MachineFilter, TechServiceFilter, ReclamationFilter

# Create your views here.


#Machine----
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



class MachineDetailView(DetailView):
    model = Machine
    context_object_name = 'macbine_detail'
    template_name = ''
    queryset = Machine.objects.all()


#TO----
class TechServiceView(ListView):
    model = TechService
    ordering = 'service_date'
    template_name = ''
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


class TechServiceDetail(DetailView):
    model = TechService
    context_object_name = 'tech_service_view'
    template_name = ''
    queryset = TechService.objects.all()


#Reclamation----
class ReclamationView(ListView):
    model = Reclamation
    ordering = 'workoff_date'
    template_name = ''
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
    context_object_name = 'reclamation_view'
    template_name = ''
    queryset = Reclamation.objects.all()