from django.urls import path
from .views import create_application_view, delete_application_view, update_view, all_applications_view, detail_view

urlpatterns = [
    path('/create', create_application_view),
    path('/all', all_applications_view),
    path('/details/<int:id>', detail_view),
    path('/delete/<int:id>', delete_application_view),
    path('/update/<int:id>', update_view),
]
