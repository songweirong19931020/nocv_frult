from django.db import models
import django.utils.timezone as timezone
# Create your models here.
class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=False)
    password = models.CharField(max_length=256)
    phone = models.IntegerField()
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]


class Goods(models.Model):
    id = models.IntegerField(primary_key=True)
    fru_name = models.CharField(max_length=50,verbose_name='菜名')
    cash = models.CharField(max_length=50,verbose_name='价格\元')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firsttype

    class Meta:
        ordering = ["fru_name"]
        verbose_name = "分类表"


class User_goods_customer(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=False)
    phone = models.IntegerField(default=50)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    fru_name = models.CharField(max_length=50)
    path_home = models.CharField(max_length=300)
    c_time = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.name


class User_goods_customers(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=False)
    phone = models.IntegerField(default=50)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    fru_name = models.CharField(max_length=50)
    path_home = models.CharField(max_length=300)
    c_time = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.name