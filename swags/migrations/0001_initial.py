# Generated by Django 4.2.7 on 2023-11-02 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Swag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='swags')),
                ('points', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SwagAward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivered', models.BooleanField(default=False)),
                ('swag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swags.swag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='swag',
            name='awarded',
            field=models.ManyToManyField(related_name='awarded_swags', through='swags.SwagAward', to=settings.AUTH_USER_MODEL),
        ),
    ]
