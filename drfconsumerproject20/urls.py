"""
URL configuration for drfconsumerproject20 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from drfconsumerapp20 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/getall',views.getallemployees, name="getallemployees"),
    path('employee/create',views.Employee_create, name="Employee_create"),
    path('employee/details/<int:employee_id>/',views.Employee_Details, name="Employee_Details"),
    path('employee/delete/<int:employee_id>/',views.Employee_Delete, name="Employee_Delete"),
    path('employee/update/<int:employee_id>/',views.Employee_Update, name="Employee_Update"),




]
