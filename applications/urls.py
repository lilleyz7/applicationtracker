from django.urls import path
from .views import create_application_view, delete_application_view, all_applications_view

urlpatterns = [
    path('create/', create_application_view),
    path('all/', all_applications_view),
    # path('details/<int:app_id>/', detail_view),
    path('delete/<int:app_id>/', delete_application_view),
    # path('update/<int:app_id>/', update_view),
]
