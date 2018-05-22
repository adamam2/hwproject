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
    path('sshkey/', TemplateView.as_view(template_name='sshkey.html'),
         name='sshkey'),
    path('downloads/', TemplateView.as_view(template_name='downloads.html'),
         name='downloads'),
    path('concepts/<slug>', views.concept_detail, name='concept_detail'),
    path('concepts/<slug>/edit/', views.edit_concept, name='edit_concept'),
    path('admin/', admin.site.urls),
]
