# Generated by Django 3.0.4 on 2020-04-25 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countries', models.CharField(max_length=500)),
                ('numbers', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Chart',
            },
        ),
        migrations.CreateModel(
            name='DataProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('file', models.FileField(upload_to='media/')),
                ('body', models.TextField()),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'DataProcess',
            },
        ),
        migrations.CreateModel(
            name='MessageUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email1', models.EmailField(max_length=254)),
                ('yMessage', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.FileField(upload_to='media/')),
                ('content', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Market',
        ),
    ]
