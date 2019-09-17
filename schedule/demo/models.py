from django.db import models
from django.utils.timezone import now
# Create your models here.
class DemoModel(models.Model):
    title=models.CharField(max_length=32,blank=True,verbose_name="标题")
    content=models.TextField(verbose_name='正文内容',blank=True,null=True,default="")
    todo_statu=models.BooleanField(default=False,verbose_name="完成状况")
    create_time=models.DateTimeField(default=now,verbose_name="创建时间")

    def __str__(self):
        return "标题;{}，当前处理状态;{}".format(self.title, self.todo_statu)

