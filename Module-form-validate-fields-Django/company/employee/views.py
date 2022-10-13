from django.shortcuts import render
from .forms import employeeregistration

# Create your views here.
def showdata(request):
    fm = employeeregistration() # this will show the empty form at the start
    if request.method=="POST": 
        fm = employeeregistration(request.POST)
        if fm.is_valid():
            print('name',fm.cleaned_data['name'])
            print('empid',fm.cleaned_data['empid'])
            print('salary',fm.cleaned_data['salary'])
            print('salarydate',fm.cleaned_data['salarydate'])
            print('available',fm.cleaned_data['available'])
            print('title',fm.cleaned_data['title'])
            print('description',fm.cleaned_data['description'])
            print('views',fm.cleaned_data['views'])
            print('agree',fm.cleaned_data['agree'])
        else:
            fm=employeeregistration()
    return render(request,'employee/home.html',{'fm':fm})
