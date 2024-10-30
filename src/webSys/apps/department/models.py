from django.db import models

# Create your models here.
class Base(models.Model):
    """ 基表 不会实际创建表"""
    class Meta:
        abstract = True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Department(Base):
    """ 部门表 """
    class Meta:
        db_table = "t_department"
        verbose_name = "部门"
        verbose_name_plural = verbose_name
    name = models.CharField(max_length=32, unique=True, verbose_name="部门名称")
    def __str__(self):
        return f"{self.name}"

