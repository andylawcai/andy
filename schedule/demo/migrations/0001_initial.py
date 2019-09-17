# Generated by Django 2.2.5 on 2019-09-09 12:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DemoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=32, verbose_name='标题')),
                ('content', models.TextField(blank=True, default='', null=True, verbose_name='正文内容')),
                ('todo_statu', models.BooleanField(default=False, verbose_name='完成状况')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
        ),
    ]
