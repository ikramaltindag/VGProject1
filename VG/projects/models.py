from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    creator = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    client = models.ForeignKey('client',on_delete=models.CASCADE)
    definition = models.TextField(null=True)
    duration_in_days = models.PositiveIntegerField()
    start_date = models.DateField(null=True)
    deadline = models.DateField(null=True)
    notes = models.TextField(null=True)
    STATUS_CHOICE = (('Completed','Completed'),('Ongoing','Ongoing'))
    status = models.CharField(max_length=9,choices=STATUS_CHOICE,blank=False)
    APPROVAL_STATUS = (('approved','approved'),('unapproved','unapproved'))
    approval_status = models.CharField(max_length=10,choices=APPROVAL_STATUS,blank=False)
    #created_at=models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Client(models.Model):
    creator = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=12)
    notes = models.TextField(null=True)

    def get_absolute_url(self):
        return reverse("client_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.name
