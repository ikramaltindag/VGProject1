from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    creator = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    # senaryomuzda sadece 3 user var (User1,User2,User3) ve bu formu doldurup onay silsilesini baslatma isini sadece User1 yapabilir.
    # o yuzden creator sadece User1 olabilir

    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    client = models.ForeignKey('client',on_delete=models.CASCADE)
    definition = models.TextField(null=True)
    duration_in_days = models.PositiveIntegerField()
    start_date = models.DateField(null=True)
    deadline = models.DateField(null=True)
    notes = models.TextField(null=True)
    design_document = # buraya dokuman ekleme ozelligi getirebiliriz. bu alana dokuman ekleme yetkisi de sadece User2'de olsun

    material_list = # buraya dokuman ekleme ozelligi getirebiliriz. bu alana dokuman ekleme yetkisi de sadece User3'te olsun
    
    current_status = ('User1','User2','User3','completed')
    #bunun amaci is suan kimde bekliyor, onu gormek

    next_status = ('User2','User3','completed')
    #bunun amaci da current_statusteki user onayladiginda is kime gidecek, onu gormek. 

    previous_status = ('User1','User2','User3')
    #bunun amaci da current_statusteki user reddettiginde is kime gidecek, onu gormek
    
    def change_status(curent_status,next_status,project):
        project=Project.object.get(project)
        
        def approve(self):
            current_user = #bir sonraki user olacak. User3 onayladiginda ise otomatik olarak completed'a donecek
        
        def reject(self):
            current_user = #bir sonraki user olacak. User1 icin reddetme secenegi olmayacak dogal olarak

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
