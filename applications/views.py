from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ApplicationForm
from .models import Application
from django.core.cache import cache

# Create your views here.
LOGIN_URL = "/auth/login/"
@login_required(login_url=LOGIN_URL)
def create_application_view(request):
    if request.method == 'POST':
        app_form = ApplicationForm(request.POST)
        if app_form.is_valid():
            app = app_form.save(commit=False)
            try:
                app.user = request.user
                app.save()
                cache.delete(f'Apps_{request.user.id}')
                return redirect('../../app/all/')
            except Exception as e:
                form = ApplicationForm()
                return render(request, 'applications/add_application.html', {'error_message': e, 'add_app_form': form})
        return render(request, 'applications/add_application.html', {'error_message': "invalid form", 'add_app_form': form})
    else:
        form = ApplicationForm()
        return render(request, 'applications/add_application.html', {'add_app_form': form})
@login_required(login_url=LOGIN_URL)
def all_applications_view(request):
    user = request.user
    try:
        applications = cache.get(f'Apps_{user.id}')
        if not applications:
            applications = Application.objects.filter(user=user)
            cache.set(f'Apps_{user.id}', applications, 60 * 20) 
            print(f'Set cache for application {user.id}')
        return render(request, 'applications/all_applications.html', {'applications': applications})
    except Exception as e:
        return render(request, 'applications/all_applications.html', {'error_message': e})

@login_required(login_url=LOGIN_URL)
def detail_view(request, app_id):
    user = request.user
    app = cache.get(f'Details_{app_id}')
    if not app:
        app = Application.objects.filter(user=user, id=app_id).first()
        cache.set(f'Details_{app_id}', app, 60 * 20)  # Cache for 20 minutes if not found in cache.
        print(f'Set cache for application {app_id}')
    return render(request, 'applications/details.html', {'application': app})

@login_required(login_url=LOGIN_URL)
def delete_application_view(request, app_id):
    user = request.user
    try:
        app = Application.objects.filter(user=user, id=app_id)
        app.delete()
        cache.delete(f'Details_{app_id}')
        cache.delete(f'Apps_{user.id}')  # Delete cache for all applications when a single application is deleted.
        print(f'Delete cache for application {app_id}')
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
            cache.delete(f'Details_{app_id}')
            cache.delete(f'Apps_{request.user.id}')
            print(f'Delete cache for application {app_id}')
            return redirect('user_applications')
    else:
        form = ApplicationForm(instance=application)

    return render(request, 'applications/update_application.html', {'form': form, 'app': application})