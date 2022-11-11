from rest_framework import serializers
from API.models import Company,Employee

# create serliazers here 
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_ID = serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"
# we are serializing model hence using model serializer 
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields='__all__'
