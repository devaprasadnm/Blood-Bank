# Generated by Django 3.2.6 on 2021-10-03 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0004_remove_donor_list_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
            ],
        ),
    ]
