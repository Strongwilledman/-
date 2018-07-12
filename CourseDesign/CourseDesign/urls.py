"""CourseDesign URL Configuration

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
from django.contrib import admin
from django.urls import path
from ManageSystem import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'login.html',views.Login.as_view()),
    path(r'logout.html',views.logout),
    path(r'index.html',views.index),
    path(r'classes.html',views.handle_classes),
    path(r'student.html',views.handle_student),
    path(r'teacher.html',views.handle_teacher),
    path(r'add_student.html',views.add_student),
    path(r'edit_student.html',views.edit_student),
    path(r'add_teacher.html',views.add_teacher),
    path(r'edit_teacher-<nid>.html', views.edit_teacher),
]
