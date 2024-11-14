from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
LOGIN_URL = "/auth/login/"
# create application
@login_required(login_url=LOGIN_URL)
def create_application_view(request):
    user = request.user
# view all apps
@login_required(login_url=LOGIN_URL)
def all_applications_view(request):
    user = request.user
# detail view 
@login_required(login_url=LOGIN_URL)
def detail_view(request):
    user = request.user
# delete application
@login_required(login_url=LOGIN_URL)
def delete_application_view(request):
    user = request.user
# update application
@login_required(login_url=LOGIN_URL)
def update_view(request):
    user = request.users