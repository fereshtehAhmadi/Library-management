# Generated by Django 3.2.13 on 2022-07-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanmodel',
            name='payment_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]