# Generated by Django 4.2.7 on 2024-02-24 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_userconfig_campus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userconfig',
            name='campus',
            field=models.CharField(blank=True, choices=[('MITS', 'MITS'), ('GEC Kannur', 'GEC Kannur'), ('Sullamus', 'Sullamus'), ('Karunagapally', 'Karunagapally'), ('Christ', 'Christ'), ('Vadakara', 'Vadakara')], max_length=100, null=True),
        ),
    ]
