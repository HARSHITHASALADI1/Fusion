# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11.23 on 2019-10-19 05:13
=======
# Generated by Django 1.11.4 on 2019-09-28 12:08
>>>>>>> 0ef4fad85c417b8840ac07a679bf8a172449df01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic_information', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('globals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Change_office',
            fields=[
                ('id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('open', 'Open'), ('confirmed', 'Confirmed'), ('rejected', 'Rejected')], default='open', max_length=50)),
                ('date_request', models.DateTimeField(blank=True, default=django.utils.timezone.now, max_length=50)),
                ('date_approve', models.DateTimeField(blank=True, max_length=50)),
                ('remarks', models.CharField(max_length=256, null=True)),
            ],
            options={
                'db_table': 'Change_office',
            },
        ),
        migrations.CreateModel(
            name='Club_budget',
            fields=[
                ('id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('budget_for', models.CharField(max_length=256)),
                ('budget_amt', models.IntegerField(default=0)),
                ('budget_file', models.FileField(upload_to='uploads/')),
                ('description', models.TextField(max_length=256)),
                ('status', models.CharField(choices=[('open', 'Open'), ('confirmed', 'Confirmed'), ('rejected', 'Rejected')], default='open', max_length=50)),
                ('remarks', models.CharField(max_length=256, null=True)),
            ],
            options={
                'db_table': 'Club_budget',
            },
        ),
        migrations.CreateModel(
            name='Club_info',
            fields=[
                ('club_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('club_website', models.CharField(default='hello', max_length=150, null=True)),
                ('category', models.CharField(choices=[('Technical', 'Technical'), ('Sports', 'Sports'), ('Cultural', 'Cultural')], max_length=50)),
                ('club_file', models.FileField(null=True, upload_to='gymkhana/club_poster')),
                ('activity_calender', models.FileField(default=' ', null=True, upload_to='gymkhana/activity_calender')),
                ('description', models.TextField(max_length=256, null=True)),
                ('alloted_budget', models.IntegerField(default=0, null=True)),
                ('spent_budget', models.IntegerField(default=0, null=True)),
                ('avail_budget', models.IntegerField(default=0, null=True)),
                ('status', models.CharField(choices=[('open', 'Open'), ('confirmed', 'Confirmed'), ('rejected', 'Rejected')], default='open', max_length=50)),
                ('co_coordinator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coco_of', to='academic_information.Student')),
                ('co_ordinator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='co_of', to='academic_information.Student')),
                ('faculty_incharge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_incharge_of', to='globals.Faculty')),
            ],
            options={
                'db_table': 'Club_info',
            },
        ),
        migrations.CreateModel(
            name='Club_member',
            fields=[
                ('id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=256, null=True)),
                ('status', models.CharField(choices=[('open', 'Open'), ('confirmed', 'Confirmed'), ('rejected', 'Rejected')], default='open', max_length=50)),
                ('remarks', models.CharField(max_length=256, null=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='this_club', to='gymkhana.Club_info')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_of', to='academic_information.Student')),
            ],
            options={
                'db_table': 'Club_member',
            },
        ),
        migrations.CreateModel(
            name='Club_report',
            fields=[
                ('id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, max_length=50)),
                ('event_details', models.FileField(upload_to='uploads/')),
                ('description', models.TextField(max_length=256, null=True)),
                ('club', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='gymkhana.Club_info')),
                ('incharge', models.ForeignKey(max_length=256, on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo')),
            ],
            options={
                'db_table': 'Club_report',
            },
        ),
        migrations.CreateModel(
            name='Core_team',
            fields=[
                ('id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('team', models.CharField(max_length=50)),
                ('year', models.DateTimeField(max_length=6, null=True)),
                ('fest_name', models.CharField(choices=[('Abhikalpan', 'Abhikalpan'), ('Gusto', 'Gusto'), ('Tarang', 'Tarang')], max_length=256)),
                ('pda', models.TextField(max_length=256)),
                ('remarks', models.CharField(max_length=256, null=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_for', to='academic_information.Student')),
            ],
            options={
                'db_table': 'Core_team',
            },
        ),
        migrations.CreateModel(
            name='Fest_budget',
            fields=[
                ('id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('fest', models.CharField(choices=[('Abhikalpan', 'Abhikalpan'), ('Gusto', 'Gusto'), ('Tarang', 'Tarang')], max_length=50)),
                ('budget_amt', models.IntegerField(default=0)),
                ('budget_file', models.FileField(upload_to='uploads/')),
                ('year', models.CharField(max_length=10, null=True)),
                ('description', models.TextField(max_length=256)),
                ('status', models.CharField(choices=[('open', 'Open'), ('confirmed', 'Confirmed'), ('rejected', 'Rejected')], default='open', max_length=50)),
                ('remarks', models.CharField(max_length=256, null=True)),
            ],
            options={
                'db_table': 'Fest_budget',
            },
        ),
        migrations.CreateModel(
            name='Other_report',
            fields=[
                ('id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, max_length=50)),
                ('event_details', models.FileField(upload_to='uploads/')),
                ('description', models.TextField(max_length=256, null=True)),
                ('incharge', models.ForeignKey(max_length=256, on_delete=django.db.models.deletion.CASCADE, to='globals.ExtraInfo')),
            ],
            options={
                'db_table': 'Other_report',
            },
        ),
        migrations.CreateModel(
            name='Session_info',
            fields=[
                ('id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('venue', models.CharField(choices=[('Classroom', (('CR101', 'CR101'), ('CR102', 'CR102'))), ('Lecturehall', (('L101', 'L101'), ('L102', 'L102')))], max_length=50)),
                ('date', models.DateField(default=None)),
                ('start_time', models.TimeField(default=None)),
                ('end_time', models.TimeField(default=None, null=True)),
                ('session_poster', models.FileField(blank=True, upload_to='gymkhana/session_poster')),
                ('details', models.TextField(max_length=256, null=True)),
                ('status', models.CharField(choices=[('open', 'Open'), ('confirmed', 'Confirmed'), ('rejected', 'Rejected')], default='open', max_length=50)),
                ('club', models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='gymkhana.Club_info')),
            ],
            options={
                'db_table': 'Session_info',
            },
        ),
        migrations.AddField(
            model_name='club_budget',
            name='club',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='gymkhana.Club_info'),
        ),
        migrations.AddField(
            model_name='change_office',
            name='club',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='gymkhana.Club_info'),
        ),
        migrations.AddField(
            model_name='change_office',
            name='co_coordinator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coco_of', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='change_office',
            name='co_ordinator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='co_of', to=settings.AUTH_USER_MODEL),
        ),
    ]
