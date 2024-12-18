from django.urls import path
from .views import create_application_view, delete_application_view, all_applications_view, update_application_view, detail_view

urlpatterns = [
    path('create/', create_application_view, name='create_application'),
    path('all/', all_applications_view, name='all_applications'),
    path('details/<int:app_id>/', detail_view, name='application_details'),
    path('delete/<int:app_id>/', delete_application_view, name='delete_application'),
    path('update/<int:app_id>/', update_application_view, name='update_application'),
]
