from django.shortcuts import render, redirect

# Create your views here.
from employee.models import Employee
from department.models import Department

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/list.html', {"employees": employees})

from django.views import  View
class EmployeeView(View):
    def get(self, request):
        content = {
            "sex_choices": Employee.sex_choices,
            "departments": Department.objects.all()
        }
        return render(request, "employee/add.html", content)

    def post(self, request):
        name = request.POST.get("name")
        password = request.POST.get("password")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        salary = request.POST.get("salary")
        department = Department.objects.get(id=request.POST.get("department_id"))

        Employee.objects.create(name=name,password=password, age=age, salary=salary, department=department)

        return redirect("/employee/list/")

from django import  forms
class Form(forms.ModelForm):
    name = forms.CharField(min_length=3, max_length=32, error_messages={
            'min_length':'用户名最小需大于3个字符','max_length':'用户名最大需小于32个字符',
            'required':'用户名不能为空'	}
            )
    class Meta:
        model = Employee
        fields = ['name', 'password', 'age', 'gender', 'salary', 'department', 'offer_at']
        # widgets = {
        #     "name": forms.TextInput(attrs={'class': 'form-control'}),
        #     "age": forms.TextInput(attrs={'class': 'form-control'}),
        # }
    def __init__(self, *args, **kwargs):
        # super(Form, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        # for field in self.fields:
        #     self.fields[field].widget.attrs = {'class': 'form-control'}
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', "placeholder": field.label}

class  EmployeeFormView(View):
    def get(self, request):
        form = Form()
        return render(request, "employee/addform.html", {"form": form})
    def post(self, request):
        form = Form(data=request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect("/employee/list/")
        else:
            print(form.errors)
            return render(request, "employee/addform.html", {"form": form})

class EmployeeDetailView(View):
    def get(self, request, id):
        employee = Employee.objects.get(id=id)
        form = Form(instance=employee)
        return render(request, 'employee/edit.html', {"form": form})

    def post(self, request, id):
        e = Employee.objects.get(id=id)
        form = Form(data=request.POST, instance=e) # 更新
        if form.is_valid():
          # form.instance.xx = xxx # 用于设置额外的字段
          form.save()
          return  redirect("/employee/list/")
        else:
            return render(request, 'employee/edit.html', {"form": form})

def EmployeeDelete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return  redirect("/employee/list/")

