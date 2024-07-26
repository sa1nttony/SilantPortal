from django.urls import path

from .views import TechServiceView, TechServiceDetail, TechServiceUpdate, TechServiceDelete, TechServiceCreate


urlpatterns = [
    path('', TechServiceView.as_view(), name='tech_services'),
    path('create/', TechServiceCreate.as_view(), name='tech_services_create'),
    path('<int:pk>', TechServiceDetail.as_view(), name='tech_service_detail'),
    path("<int:pk>/update/", TechServiceUpdate.as_view(), name='tech_service_update'),
    path("<int:pk>/delete", TechServiceDelete.as_view(), name='tech_service_delete'),
]
