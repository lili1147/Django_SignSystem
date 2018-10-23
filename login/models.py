from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=50,verbose_name="发布会名称")
    limit = models.IntegerField(default=0,verbose_name='最大人数')
    status = models.BooleanField(verbose_name='是否举行')
    address = models.CharField(max_length=100,verbose_name='地址')
    start_time = models.DateTimeField(verbose_name='时间')
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Guest(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    realname = models.CharField(max_length=20,verbose_name='嘉宾姓名')
    phone = models.CharField(max_length=16,verbose_name='电话')
    email = models.EmailField(verbose_name='邮箱')
    sign  = models.BooleanField(verbose_name='是否签到')
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('event','phone')

    def __str__(self):
        return self.realname