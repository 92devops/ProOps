import math

from django.shortcuts import render, redirect

# Create your views here.
from django.utils.safestring import mark_safe
from django.views import View
from mobile.models import Mobile
from .pagination import  Pagination


def mobile_list(request):
    data_dict = {}
    search_data=request.GET.get("q","")
    if search_data:
        data_dict["mobile_num__contains"] = search_data
        data = Mobile.objects.filter(**data_dict).order_by("-level")
        page_object = Pagination(request, data, search_data)  # 其他三个参数根据需求调整
        context = {
            "mobiles": page_object.data,
            "search_data": search_data,
            "page_string": page_object.Html(),
            "search_data": search_data
        }
        return render(request, "mobile/list.html", context)

    data = Mobile.objects.filter(**data_dict).order_by("-level")
    page_object = Pagination(request, data, search_data)  # 其他三个参数根据需求调整
    context = {
        "mobiles": page_object.data,
        "search_data": search_data,
        "page_string": page_object.Html(),
        "search_data": search_data
    }
    return render(request, "mobile/list.html",context)


from .forms import  MobileForm,MobileEditForm
class  MobileView(View):
    def get(self, request):
        form = MobileForm()
        return render(request, "mobile/add.html", {"form": form})
    def post(self, request):
        form = MobileForm(data=request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect("/mobile/list/")
        else:
            print(form.errors)
            return render(request, "mobile/add.html", {"form": form})

class MobileDetailView(View):
    def get(self, request, id):
        employee = Mobile.objects.get(id=id)
        form = MobileEditForm(instance=employee)
        return render(request, 'mobile/edit.html', {"form": form})

    def post(self, request, id):
        e = Mobile.objects.get(id=id)
        form = MobileEditForm(data=request.POST, instance=e)  # 更新
        if form.is_valid():
            # form.instance.xx = xxx # 用于设置额外的字段
            form.save()
            return redirect("/mobile/list/")
        else:
            return render(request, 'mobile/edit.html', {"form": form})

def MobileDelete(request, id):
    employee = Mobile.objects.get(id=id)
    employee.delete()
    return redirect("/mobile/list/")