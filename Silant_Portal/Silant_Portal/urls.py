"""
URL configuration for Silant_Portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('loader_service.urls_auth')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('home/', include('loader_service.urls'), name='home'),
    path('tech_services/', include('loader_service.urls_ts')),
    path('reclamations/', include('loader_service.urls_reclamations')),
    path('logout/', LogoutView.as_view(next_page='/home/'), name='logout'),
    path('administration/', include('loader_service.urls_administration')),
]
