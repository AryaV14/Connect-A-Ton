# Generated by Django 4.2.7 on 2024-02-24 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_useranswer_skipped'),
    ]

    operations = [
        migrations.AddField(
            model_name='userconfig',
            name='campus',
            field=models.CharField(choices=[('MITS', 'MITS'), ('GEC Kannur', 'GEC Kannur'), ('Sullamus', 'Sullamus'), ('Karunagapally', 'Karunagapally'), ('Christ', 'Christ'), ('Vadakara', 'Vadakara')], default=' ', max_length=100),
        ),
    ]
