from django.urls import path
from . import  views
urlpatterns = [
    path('', views.index, name="index"),
    path("department/list/", views.department_list, name="department_list"),
    path("department/add/", views.DepartmentView.as_view(), name="department_add"),
    path("department/edit/<int:id>/", views.DepartmentDetailView.as_view(), name="department_edit"),
    path("department/del/<int:id>/", views.DepartmentDelete, name="department_del"),
]
