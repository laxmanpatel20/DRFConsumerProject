from django.shortcuts import redirect, render
import requests

from drfconsumerapp20.forms import EmployeeForm
# Create your views here.

API_BASE_URL = "http://localhost:8000/api/viewsetemployees/"

def getallemployees(request):


    response = requests.get(f"{API_BASE_URL}")

    if response.status_code == 200:
        try:
            employees= response.json()
        except ValueError:
            employees = []
    else:
        employees = []
    
    return render(request, 'Employee.html', {'employees':employees})


def Employee_create(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            requests.post(url="http://localhost:8000/api/viewsetemployees/", data=form.data)
        return redirect("getallemployees")
    return render(request, "Employee_insert.html", {"form":form})



def Employee_Details(request, employee_id):

    response = requests.get("http://localhost:8000/api/viewsetemployees/" + f"{employee_id}/")
    
    response_data = response.json()

    form = EmployeeForm(
        response_data,
        initial={
            "Department": response_data.get("Department"),
            "Country": response_data.get("Country"),
        },
    )

    return render(request, "EmployeeDetails.html",{"form":form})
        

def Employee_Delete(request, employee_id):

    response = requests.get("http://localhost:8000/api/viewsetemployees/" + f"{employee_id}/")

    response_data = response.json()

    form = EmployeeForm(
        response_data,
        initial={
            "Department": response_data.get("Department"),
            "Country":response_data.get("Country"),
        }
    )
    if request.method == "POST":
        requests.delete(
            url="http://localhost:8000/api/viewsetemployees/" + f"{employee_id}/"
        )
        return redirect("getallemployees")

    return render(request, "EmployeeDelete.html" ,{"form":form})


def Employee_Update(request, employee_id):
    
    response = requests.get("http://localhost:8000/api/viewsetemployees/" + f"{employee_id}/")

    response_data = response.json()

    form = EmployeeForm(
        response_data,
        initial={
            "Department": response_data.get("Department"),
            "Country":response_data.get("Country"),
        }
    )
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        requests.put(
            url="http://localhost:8000/api/viewsetemployees/" + f"{employee_id}/",data=form.data
        )
        return redirect("getallemployees")

    return render(request, "EmployeeUpdate.html" ,{"form":form})
