from django.shortcuts import render
from test2.models import test2model
from test2.models import test3model

# Create your views here.
def test2data(request):
    test2_list=test2model.objects.all() # all data goes to test2 list
    test3_list=test3model.objects.all()
    return render(request, 'test2/home.html',{'test2_list':test2_list, 'test3_list':test3_list})

# def test3data(request):
#     test3_list=test3model.objects.all() # all data goes to test3 list
#     return render(request, 'test2/home.html',{'test3_list':test3_list})