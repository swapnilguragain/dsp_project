# Generated by Django 4.2.7 on 2023-12-06 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0007_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='firstName',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='patient',
            name='healthHistory',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='lastName',
            field=models.CharField(max_length=500),
        ),
    ]
