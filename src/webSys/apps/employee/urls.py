

from django.urls import path
from . import  views
urlpatterns = [
    path("employee/list/", views.employee_list, name="employee_list"),
    path("employee/add/", views.EmployeeView.as_view(), name="employee_add"),

    path("employee/addform/", views.EmployeeFormView.as_view(), name="employee_addform"),

    path("employee/edit/<int:id>/", views.EmployeeDetailView.as_view(), name="employee_edit"),
    path("employee/del/<int:id>/", views.EmployeeDelete, name="department_del"),
]