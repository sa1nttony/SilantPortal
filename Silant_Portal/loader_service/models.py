import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save

from django_lifecycle import LifecycleModel, hook, AFTER_CREATE, AFTER_UPDATE

# Create your models here.


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

    # @hook(AFTER_CREATE)
    # def add_group(self):
    #     if self.role == 'CL':
    #         group = Group.objects.get(name='Clients')
    #         Profile.objects.get(pk=self.pk).groups.add(group)
    #     elif self.role == 'SR':
    #         group = Group.objects.get(name='Service companies')
    #         group.user_set.add(Profile.objects.get(pk=self.pk))
    #     elif self.role == 'MG':
    #         group = Group.objects.get(name='Managers')
    #         group.user_set.add(Profile.objects.get(pk=self.pk))


@receiver(post_save, sender=Profile)
def add_group(sender, instance, created, **kwargs):
    if instance.role == 'CL':
        group = Group.objects.get(name='Clients')
        Profile.objects.get(pk=instance.pk).groups.add(group)
    elif instance.role == 'SR':
        group = Group.objects.get(name='Service companies')
        Profile.objects.get(pk=instance.pk).groups.add(group)
    elif instance.role == 'MG':
        group = Group.objects.get(name='Managers')
        Profile.objects.get(pk=instance.pk).groups.add(group)


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
    options = models.TextField(blank=True)
    client = models.ForeignKey(Profile, on_delete=models.CASCADE)
    service_company = models.ForeignKey("ServiceCompany", on_delete=models.CASCADE)

    def __str__(self):
        return f'Модель {self.equipment_model} №{self.equipment_number}'


#ТО
class TechService(models.Model):
    service_type = models.ForeignKey('ServiceType', on_delete=models.CASCADE)
    service_date = models.DateTimeField()
    mileage = models.IntegerField()
    order_number = models.CharField(max_length=256)
    order_date = models.DateField()
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    service_company = models.ForeignKey('ServiceCompany', on_delete=models.CASCADE)

    def __str__(self):
        return f"ТО {self.machine} / {self.service_date}"


class Reclamation(LifecycleModel):
    workoff_date = models.DateField()
    mileage = models.IntegerField()
    workoff_node = models.CharField(max_length=256)
    workoff_descriprion = models.TextField()
    repair_method = models.CharField(max_length=256)
    used_recovery_kit = models.CharField(max_length=256)
    repair_date = models.DateField(max_length=256)
    dead_time = models.IntegerField(null=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    service_company = models.ForeignKey('ServiceCompany', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.machine}/{self.workoff_date}/{self.workoff_node}"

    @hook(AFTER_CREATE)
    def recalculate_create(self):
        self.dead_time = (self.repair_date - self.workoff_date).days
        self.save()


#Справочники
#Модель техники
class EquipmentModel(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.title


#Модель двигателя
class EngineModel(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.title


#Модель трансмиссии
class TransmissionModel(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.title


#Модель ведущего моста
class DrivingAxleModel(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.title


#Модель управляемого моста
class ControlAxleModel(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.title


#Вид ТО
class ServiceType(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.title


#Организация проводившая ТО
class ServiceCompany(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
