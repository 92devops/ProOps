from django.urls import path
from . import  views
urlpatterns = [
    path("mobile/list/", views.mobile_list, name="mobile_list"),

    path("mobile/add/", views.MobileView.as_view(), name="mobile_add"),
    #
    path("mobile/edit/<int:id>/", views.MobileDetailView.as_view(), name="mobile_edit"),
    path("mobile/del/<int:id>/", views.MobileDelete, name="mobile_del"),
]