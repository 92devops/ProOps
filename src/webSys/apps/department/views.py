from django.shortcuts import render, redirect
from django.http import HttpRequest

# Create your views here.
from django.http import HttpRequest

def index(request:HttpRequest):
    return render(request, "index.html")

from department.models import  Department

def department_list(request):
    departments = Department.objects.all()

    return  render(request, 'department/list.html', {"departments": departments})

from django.views import  View

class DepartmentView(View):
    def get(self, request):
        return render(request, "department/add.html")

    def post(self, request):
        name = request.POST.get("department_name")
        d = Department.objects.filter(name=name)
        if d:
            return render(request, "department/add.html" ,{"msg": f"{name}已存在"})
        Department.objects.create(name=name)

        return redirect("/department/list/")

class DepartmentDetailView(View):
    def get(self, request, id):
        department = Department.objects.get(id=id)
        if department:
            id = department.id
            print(type(id))
            name = department.name
            return  render(request, "department/edit.html", {"id": id, "name": name})

    def post(self, request, id):
        department = Department.objects.get(id=id)
        name = request.POST.get("department_name",department.name )
        if name:
            department.name = name
            department.save()
            return redirect("/department/list/")
        else:
            return render(request, "department/edit.html", {"id": id, "name": name, "msg": "项目名不能为空"})

def DepartmentDelete(request, id):
    department = Department.objects.get(id=id)
    department.delete()
    return  redirect("/department/list/")
