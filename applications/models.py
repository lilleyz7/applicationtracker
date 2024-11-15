from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Application(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interviewed', 'Interviewed'),
        ('interested', 'Interested'),
        ('offered', 'Offered'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=30)
    location = models.CharField(max_length=50, blank=True )
    details = models.TextField(blank=True)
    added = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='interested')

    def __str__(self):
        return f"{self.job_title} for {self.company} in {self.location}"