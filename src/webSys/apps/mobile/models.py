import random

from django.db import models

# Create your models here.
class Mobile(models.Model):
    class Meta:
        db_table = "t_mobile"
        verbose_name = "员工"
        verbose_name_plural = verbose_name
    mobile_num = models.CharField(max_length=11, unique=True, verbose_name="手机号")
    price = models.IntegerField(default=0, verbose_name="价格")
    level_choices = (
        (1, "1级"),
        (2, "2级"),
        (3, "3级"),
    )
    level = models.SmallIntegerField(choices=level_choices, default=3, verbose_name="级别")
    status_choices = (
        (0, "未占用"),
        (1, "已占用")
    )
    status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name="状态")

    def generate_data(self):
        for i in range(0, 35):
            self.mobile_num = str(random.randint(135000000000, 189000000000))
            self.price = random.randint(10, 100)
            self.level = random.randint(1, 3)
            self.status = random.randint(0, 1)




