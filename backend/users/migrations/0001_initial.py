# Generated by Django 2.2.6 on 2019-10-30 23:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('user_type', models.CharField(choices=[('MI', 'Medical Institution'), ('CU', 'Customer')], max_length=2)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('contact_number', models.CharField(blank=True, max_length=15, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='Profile Picture')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1, null=True)),
                ('blood_type', models.CharField(blank=True, choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=3, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('points', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MedicalInstitution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='institution/logos/')),
                ('is_partner', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Incentive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('points_required', models.PositiveIntegerField()),
                ('medical_institution', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.MedicalInstitution')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=50)),
                ('event_datetime', models.DateTimeField()),
                ('contact_number', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('medical_institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.MedicalInstitution')),
            ],
        ),
        migrations.CreateModel(
            name='DonationRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('relation_to_patient', models.CharField(max_length=20)),
                ('blood_type_of_patient', models.CharField(choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=3)),
                ('is_transfusion', models.BooleanField(default=False)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.MedicalInstitution')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_blood_bags', models.PositiveIntegerField()),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.Customer')),
                ('medical_institution', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.MedicalInstitution')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('appointment_date', models.DateField()),
                ('is_willing_for_transfusion', models.BooleanField(default=False)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.Customer')),
                ('medical_institution', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.MedicalInstitution')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
