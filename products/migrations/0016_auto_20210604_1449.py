# Generated by Django 3.1b1 on 2021-06-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_remove_it_date_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='it',
            name='matric_no',
            field=models.CharField(max_length=20),
        ),
    ]
