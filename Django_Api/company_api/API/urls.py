from django.contrib import admin
from django.urls import path,include
from API.views import CompanyViewSet, EmployeeViewSet
from rest_framework import routers

# we will create router, Roy
router = routers.DefaultRouter() 
router.register(r'companies',CompanyViewSet)
router.register(r'employees',EmployeeViewSet)


urlpatterns = [
    path('',include(router.urls))
]


# companies/ID/employees