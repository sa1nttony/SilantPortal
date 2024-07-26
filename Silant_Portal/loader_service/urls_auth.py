from django.urls import path

from .views import AddUserView


urlpatterns = [
    path('add_user', AddUserView.as_view(), name='add_user')
]
