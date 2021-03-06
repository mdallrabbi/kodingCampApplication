# Generated by Django 2.0.5 on 2018-05-19 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selection_confirmation', models.BooleanField(default=False)),
                ('call_for_interview', models.BooleanField(default=False)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.PersonalProfile')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='JobPostBasic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=256)),
                ('salary_range', models.CharField(max_length=256)),
                ('is_part_time', models.BooleanField(default=False)),
                ('position', models.CharField(max_length=256)),
                ('stack', models.TextField()),
                ('vacancy', models.PositiveIntegerField()),
                ('deadline', models.DateField()),
                ('status', models.BooleanField(default=True)),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobPostDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('application_process', models.TextField()),
                ('screening_details', models.TextField()),
                ('job', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jobpost.JobPostBasic')),
            ],
        ),
        migrations.AddField(
            model_name='jobapplicant',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobpost.JobPostBasic'),
        ),
    ]
