from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ApplicationForm
from .models import Application
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

# Create your views here.
LOGIN_URL = "/auth/login/"
# create application
@login_required(login_url=LOGIN_URL)
def create_application_view(request):
    if request.method == 'POST':
        app_form = ApplicationForm(request.POST)
        if app_form.is_valid():
            app = app_form.save(commit=False)
            try:
                app.user = request.user
                app.save()
                return redirect('../../app/all/')
            except Exception as e:
                form = ApplicationForm()
                return render(request, 'applications/add_application.html', {'error_message': e, 'add_app_form': form})
        return render(request, 'applications/add_application.html', {'error_message': "invalid form", 'add_app_form': form})
    else:
        form = ApplicationForm()
        return render(request, 'applications/add_application.html', {'add_app_form': form})
# view all apps
@login_required(login_url=LOGIN_URL)
def all_applications_view(request):
    user = request.user
    try:
        applications = Application.objects.filter(user=user)
        return render(request, 'applications/all_applications.html', {'applications': applications})
    except Exception as e:
        return render(request, 'applications/all_applications.html', {'error_message': e})

# @login_required(login_url=LOGIN_URL)
# def detail_view(request, app_data):
#     user = request.user
#     app = Application.objects.filter(user=user, id=)

@login_required(login_url=LOGIN_URL)
def delete_application_view(request, app_id):
    user = request.user
    try:
        app = Application.objects.filter(user=user, id=app_id)
        app.delete()
        return redirect("/app/all/")
    except Exception as e:
        return render(request, 'applications/all_applications.html', {'error_message': e})

@login_required
def update_application_view(request, app_id):
    application = get_object_or_404(Application, id=app_id, user=request.user)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('user_applications')
    else:
        form = ApplicationForm(instance=application)

    return render(request, 'applications/update_application.html', {'form': form, 'app': application})