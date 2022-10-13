from doctest import debug_script
from django import forms

class employeeregistration(forms.Form):
    name = forms.CharField(min_length=5, max_length=50,required=True,initial='Your Name') # required field 
    empid = forms.IntegerField(min_value=5,max_value=50,label='Your emp ID')
    salary = forms.IntegerField(error_messages={'required':'enter your salary'}) # this makes the field required 
    salarydate = forms.DateField()
    available=forms.BooleanField(widget=forms.Textarea,help_text='100 characters max.')
    title = forms.CharField(widget=forms.Textarea,help_text='100 characters max.')
    description = forms.CharField(widget=forms.CheckboxInput)
    views = forms.IntegerField(widget=forms.Textarea) 
    agree = forms.BooleanField(label='I agree') # you can change the lable as per needed