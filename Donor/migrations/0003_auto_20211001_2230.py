# Generated by Django 3.2.7 on 2021-10-01 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0002_auto_20210929_1400'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user_list',
        ),
        migrations.AlterField(
            model_name='donor_list',
            name='phn',
            field=models.CharField(default=None, max_length=12),
        ),
        migrations.AlterField(
            model_name='donor_list',
            name='user_id',
            field=models.EmailField(default=None, max_length=100),
        ),
    ]
