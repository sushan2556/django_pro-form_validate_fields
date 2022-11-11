from django.shortcuts import render
from rest_framework import viewsets 
from API.models import Company,Employee
from API.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
# we will not use function based views 
# we will use django rest framework for creating views for all CRUD options 

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

    #URL created - companies/{company_id}/employees
    # for custom APIS, creating actiona as anotation 
    @action(detail=True,methods=['get']) # keeping detail true to pass primary key compulsory 
    def employees(self,request,pk=None):
        try:
            company=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=company)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response(
            {
                'message':'Company might not exist'
            }
        )


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer