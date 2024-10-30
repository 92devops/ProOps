import datetime

from django.db import models

# Create your models here.

from department.models import  Department, Base

class Employee(Base):
    """ 员工表 """
    class Meta:
        db_table = "t_employee"
        verbose_name = "员工"
        verbose_name_plural = verbose_name
    name = models.CharField(max_length=32, verbose_name="姓名")
    password = models.CharField(max_length=32, verbose_name="密码")
    age = models.IntegerField(default=1, verbose_name="年龄")
    sex_choices = ((0, "女"), (1, "男"))
    gender = models.SmallIntegerField(choices=sex_choices, default=0, verbose_name="性别")
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="薪资")
    offer_at = models.DateField(default=datetime.datetime.now, verbose_name="入职时间")
    department = models.ForeignKey(to=Department, to_field="id", related_name="employee", on_delete=models.CASCADE, verbose_name="部门")

    def __str__(self):
        return f"<{self.name}:{self.gender}:{self.age}>"