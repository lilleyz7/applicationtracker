from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['job_title', 'company', 'listing', 'location', 'deadline', 'status']
        widgets = {
            'applied_date': forms.DateInput(attrs={'type': 'date'}),
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(choices=Application.STATUS_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['job_title'].widget.attrs.update({'placeholder': 'Job Title'})
        self.fields['company'].widget.attrs.update({'placeholder': 'Company Name'})
        self.fields['listing'].widget.attrs.update({'placeholder': 'Link to Listing'})
        self.fields['location'].widget.attrs.update({'placeholder': 'Location'})