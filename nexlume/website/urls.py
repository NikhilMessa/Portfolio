from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('project/<str:project_name>/', views.project_details, name='project_details'),
    path('services/', views.services, name='services'),
    path('team/', views.team_view, name='team'),
    path('contact/', views.contact_form, name='contact_form'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
