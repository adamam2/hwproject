"""hellowebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView
from collection import views
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
    password_change,
    password_change_done,
)
from collection.backends import MyRegistrationView

urlpatterns = [
    path('', views.index, name='home'),
    path('setup/', TemplateView.as_view(template_name='setup.html'), name='setup'),
    path('development/', TemplateView.as_view(template_name='development.html'), name='development'),
    path('webdesign/', TemplateView.as_view(template_name='webdesign.html'),
         name='webdesign'),
    path('appdesign/', TemplateView.as_view(template_name='appdesign.html'),
         name='appdesign'),
    path('database/', TemplateView.as_view(template_name='database.html'), name='database'),
    path('accessmanagement/', TemplateView.as_view(template_name='accessmanagement.html'),
         name='accessmanagement'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('reference/', TemplateView.as_view(template_name='reference.html'),
         name='reference'),
    path('commands/', TemplateView.as_view(template_name='commands.html'),
         name='commands'),
    path('sshkey/', TemplateView.as_view(template_name='sshkey.html'),
         name='sshkey'),
    path('downloads/', TemplateView.as_view(template_name='downloads.html'),
         name='downloads'),
    path('concepts/<slug>/', views.concept_detail, name='concept_detail'),
    path('concepts/<slug>/edit/', views.edit_concept, name='edit_concept'),
    
    
    path('accounts/', include('registration.backends.simple.urls')),
    
    
    path('accounts/password/reset/', password_reset,
        {'template_name': 'registration/password_reset_form.html'},
        name="password_reset"),
    path('accounts/password/reset/done/', password_reset_done,
        {'template_name': 'registration/password_reset_done.html'},
        name="password_reset_done"),
    path('accounts/password/reset/<uidb64>/<token>/', password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html'},
        name="password_reset_confirm"),
    path('accounts/password/rest/done/', password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'},
        name="password_reset_complete"),
    
    path('accounts/password/change/', password_change,
        {'template_name': 'registration/password_change_form.html'},
        name="password_change"),
    path('accounts/password/change/done', password_change_done,
         {'template_name': 'registration/password_change_done.html'},
         name="password_change_done"),


    path('accounts/register/', MyRegistrationView.as_view(),
        name="registration_register"),
    path('accounts/create_concep', views.create_concept,
        name="registration_create_concept"),
    
    path('admin/', admin.site.urls),
]
