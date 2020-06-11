from django.shortcuts import render,get_object_or_404,redirect
from projects.models import Project,Client
from projects.forms import ProjectForm,ClientForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView,ListView,
                                CreateView,UpdateView,
                                DeleteView,DetailView)
# Create your views here.

def index(request):
    return render(request,'projects/index.html')


class ProjectAllListView(ListView):
    model = Project
    # # python version of writing SQL Query
    template_name = 'projects/project_list_all.html'
    def get_queryset(self):
        return Project.objects.all()

class ProjectCompletedListView(ListView):
    model = Project
    # python version of writing SQL Query
    template_name = 'projects/project_list_completed.html'
    def get_queryset(self):
        return Project.objects.filter(status='Completed').all()

class ProjectOngoingListView(ListView):
    model = Project
    # python version of writing SQL Query
    template_name = 'projects/project_list_ongoing.html'
    def get_queryset(self):
        return Project.objects.filter(status='Ongoing').all()

class ProjectDetailView(DetailView):
    model = Project

class ProjectCreateView(LoginRequiredMixin,CreateView):
# We want this option to be available only to logedin users
# that is why we use mixin
    login_url = '/login/'
    template_name = 'projects/project_form.html'
    form_class = ProjectForm
    model = Project


class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'projects/project_detail.html'
    form_class = ProjectForm
    model = Project

class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    model = Project
    success_url = reverse_lazy('project_list_all')

class ProjectUnapprovedListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    template_name = 'projects/project_list_all.html'
    model = Project

    def get_queryset(self):
        return Project.objects.filter(approval_status='unapproved').all()

class ProjectApprovedListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    template_name = 'projects/project_list_approved.html'
    model = Project

    def get_queryset(self):
        return Project.objects.filter(approval_status='approved').all()

class ClientListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    template_name = 'projects/client_list.html'
    model = Client
    def get_queryset(self):
        return Client.objects.all()

class ClientDetailView(DetailView):
    model = Client

class ClientCreateView(LoginRequiredMixin,CreateView):
# We want this option to be available only to logedin users
# that is why we use mixin
    login_url = '/login/'
    template_name = 'projects/client_form.html'
    form_class = ClientForm
    model = Client


class ClientUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'projects/client_detail.html'
    form_class = ClientForm
    model = Client

class ClientDeleteView(LoginRequiredMixin,DeleteView):
    model = Client
    success_url = reverse_lazy('client_list')
