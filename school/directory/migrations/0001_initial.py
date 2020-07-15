# Generated by Django 3.0.8 on 2020-07-14 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('room_number', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Teacher',
            },
        ),
        migrations.CreateModel(
            name='SubjectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=15)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.TeacherModel')),
            ],
            options={
                'db_table': 'Subject',
            },
        ),
        migrations.CreateModel(
            name='ProPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propic', models.FileField(upload_to='pro_pics/')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.TeacherModel')),
            ],
            options={
                'db_table': 'ProPic',
            },
        ),
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.TeacherModel')),
            ],
            options={
                'db_table': 'Phone',
            },
        ),
    ]
