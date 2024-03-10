# Generated by Django 3.2.8 on 2021-12-11 11:11

import ckeditor.fields
import courses.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('overview', models.TextField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('feature', models.BooleanField(default=False, null=True)),
                ('photo', models.ImageField(default='courses/course_icon.png', upload_to='courses/%Y/%m/%d/')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.BooleanField(default=False, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('feature', models.BooleanField(default=False, null=True)),
                ('photo', models.ImageField(default='subjects/subjects_icon.png', upload_to='subjects/%Y/%m/%d/')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('url', models.URLField()),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_related', to='courses.instructor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text_related', to='courses.instructor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('order', courses.fields.OrderField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='courses.course')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='images')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_related', to='courses.instructor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='files')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_related', to='courses.instructor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_enrollements', to='courses.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='students.student')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
        migrations.AddField(
            model_name='course',
            name='enrollments',
            field=models.ManyToManyField(through='courses.Enrollment', to='students.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses_created', to='courses.instructor'),
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='courses.subject'),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('order', courses.fields.OrderField(blank=True)),
                ('content_type', models.ForeignKey(limit_choices_to={'model__in': ('text', 'video', 'image', 'file')}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='courses.module')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]