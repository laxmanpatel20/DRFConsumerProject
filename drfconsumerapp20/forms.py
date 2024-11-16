from django import forms 
import requests


def department_choices():
    response = requests.get("http://localhost:8000/departments_list")
    return response.json()

def country_choices():
    response = requests.get("http://localhost:8000/country_list")
    return response.json()

class EmployeeForm(forms.Form):
    FirstName = forms.CharField(max_length=30)
    LastName = forms.CharField(max_length=30)
    TitleName = forms.CharField(max_length=30)
    HasPassPort = forms.BooleanField()
    Salary = forms.IntegerField()
    HireDate = forms.DateField()
    Notes = forms.CharField(max_length=200)
    Email = forms.EmailField(max_length=20)
    PhoneNumber = forms.CharField(max_length=10)
    Department = forms.ChoiceField(choices = department_choices())
    Country = forms.ChoiceField(choices=country_choices())


    class Meta:
        fields=[
            "FirstName",
            "LastName",
            "TitleNmae",
            "HaspassPort",
            "Salary",
            "HireDate",
            "Notes",
            "Email",
            "PhoneNumber",
            "Department",
            "Country"
        ]
        widget = {
            'BrithDate': forms.widgets.DateInput(attrs={'type': 'date'}),
            'HireDate' : forms.widgets.DateInput(attrs={"type": 'date'}),
        }