# Generated by Django 3.0.5 on 2020-04-28 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='avatars')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date', django_jalali.db.models.jDateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.Profile')),
            ],
            options={
                'verbose_name_plural': 'ToDo Items',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('fa', 'Persian'), ('en', 'English')], max_length=50)),
                ('theme', models.CharField(choices=[('blue', 'Blue'), ('pink', 'Pink'), ('yellow', 'Yellow')], max_length=50)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='plan.Profile')),
            ],
        ),
    ]