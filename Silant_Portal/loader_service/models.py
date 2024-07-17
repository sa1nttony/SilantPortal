from django.db import models
from django.contrib.auth.models import AbstractUser

from django_lifecycle import LifecycleModel, hook, AFTER_CREATE, AFTER_UPDATE

# Create your models here.
#TODO Придумать как реализовать модель пользователя с разделением прав


class Profile(AbstractUser):
    client = 'CL'
    service_co = 'SR'
    manager = 'MG'
    ROLES = [
        (client, 'Клиент'),
        (service_co, 'Сервисная организация'),
        (manager, 'Менеджер'),
    ]
    role = models.CharField(max_length=2, choices=ROLES, default=client)
    bio = models.TextField(null=True)


#Машина
class Machine(models.Model):
    equipment_number = models.CharField(max_length=256, unique=True)
    equipment_model = models.ForeignKey('EquipmentModel', on_delete=models.CASCADE)
    engine_model = models.ForeignKey('EngineModel', on_delete=models.CASCADE)
    engine_number = models.CharField(max_length=256)
    transmission_model = models.ForeignKey('TransmissionModel', on_delete=models.CASCADE)
    transmission_number = models.CharField(max_length=256)
    driving_axle_model = models.ForeignKey('DrivingAxleModel', on_delete=models.CASCADE)
    driving_axle_number = models.CharField(max_length=256)
    control_axle_model = models.ForeignKey('ControlAxleModel', on_delete=models.CASCADE)
    control_axle_number = models.CharField(max_length=256)
    shipment_contract = models.CharField(max_length=256)
    shipment_out_date = models.DateField()
    consignee = models.CharField(max_length=256)
    shipment_adress = models.CharField(max_length=256)
    client = models.ForeignKey(Profile, on_delete=models.CASCADE)
    service_company = models.ForeignKey("ServiceCompany", on_delete=models.CASCADE)


#ТО
class TechService(models.Model):
    service_type = models.ForeignKey('ServiceType', on_delete=models.CASCADE)
    service_date = models.DateTimeField()
    mileage = models.IntegerField()
    order_number = models.CharField(max_length=256)
    order_date = models.DateField()
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    service_company = models.ForeignKey('ServiceCompany', on_delete=models.CASCADE)


class Reclamation(models.Model):
    workoff_date = models.DateField()
    mileage = models.IntegerField()
    workoff_node = models.CharField(max_length=256)
    workoff_descriprion = models.TextField()
    repair_method = models.CharField(max_length=256)
    used_recovery_kit = models.CharField(max_length=256)
    repair_date = models.DateField(max_length=256)
    dead_time = models.IntegerField()
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    service_company = models.ForeignKey('ServiceCompany', on_delete=models.CASCADE)

    # TODO написать метод, который будет считать время по формуле recovery_date - workoff_date. Проверить его работу
    def count_dead_time(self):
        self.dead_time = self.repair_date - self.workoff_date


#Справочники
#Модель техники
class EquipmentModel(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()


#Модель двигателя
class EngineModel(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()


#Модель трансмиссии
class TransmissionModel(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()


#Модель ведущего моста
class DrivingAxleModel(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()


#Модель ведущего моста
class ControlAxleModel(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()


#Вид ТО
class ServiceType(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()


#Организация проводившая ТО
class ServiceCompany(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
