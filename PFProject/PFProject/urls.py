"""
URL configuration for PFProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from PFApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info', views.info, name='info'),
    path('project', views.project, name='project'),
    path('blog', views.blog, name='blog'),
    path('new/', views.new, name='new'),
    path('detail/<int:article_id>', views.detail, name='detail'),
    path('category/<int:category_id>/', views.category, name='category'),

]

from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)