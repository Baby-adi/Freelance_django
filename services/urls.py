from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service_list'),              # List all services
    path('create/', views.service_create, name='service_create'),   # Create a new service
    path('<int:pk>/update/', views.service_update, name='service_update'),  # Update a service
    path('<int:pk>/delete/', views.service_delete, name='service_delete'),  # Delete a service
]