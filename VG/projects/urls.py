from django.urls import path
from projects import views

urlpatterns = [
    path('',views.index,name='index'),
    path('projects/all',views.ProjectAllListView.as_view(),name='project_list_all'),
    path('project/create/', views.ProjectCreateView.as_view(), name='project_create'),
    path('projects/completed',views.ProjectCompletedListView.as_view(),name='project_list_completed'),
    path('projects/ongoing',views.ProjectOngoingListView.as_view(),name='project_list_ongoing'),
    path('projects/unapproved',views.ProjectUnapprovedListView.as_view(),name='project_list_unapproved'),
    path('projects/approved',views.ProjectApprovedListView.as_view(),name='project_list_approved'),

    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project_detail'),
    path('project/<int:pk>/update/', views.ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),

    path('clients/all',views.ClientListView.as_view(),name='client_list'),
    path('client/create/', views.ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>', views.ClientDetailView.as_view(), name='client_detail'),

    path('client/<int:pk>/update', views.ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client_delete'),


]
