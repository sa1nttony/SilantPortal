from django.contrib import admin
from .models import Profile, Machine, TechService, Reclamation, EquipmentModel, EngineModel, TransmissionModel, DrivingAxleModel, ControlAxleModel, ServiceType, ServiceCompany

# Register your models here.
admin.site.register(Profile)
admin.site.register(Machine)
admin.site.register(TechService)
admin.site.register(Reclamation)
admin.site.register(EquipmentModel)
admin.site.register(EngineModel)
admin.site.register(TransmissionModel)
admin.site.register(DrivingAxleModel)
admin.site.register(ControlAxleModel)
admin.site.register(ServiceType)
admin.site.register(ServiceCompany)