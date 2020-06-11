# Generated by Django 3.0.7 on 2020-06-11 00:26

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
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_person', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=12)),
                ('notes', models.TextField(null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('definition', models.TextField(null=True)),
                ('duration_in_days', models.PositiveIntegerField()),
                ('start_date', models.DateField(null=True)),
                ('deadline', models.DateField(null=True)),
                ('notes', models.TextField(null=True)),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Ongoing', 'Ongoing')], max_length=9)),
                ('approval_status', models.CharField(choices=[('approved', 'approved'), ('unapproved', 'unapproved')], max_length=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Client')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]