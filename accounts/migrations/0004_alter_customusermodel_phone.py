# Generated by Django 3.2 on 2022-06-11 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customusermodel_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='phone',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
