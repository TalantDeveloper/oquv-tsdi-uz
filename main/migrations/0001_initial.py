# Generated by Django 4.2.4 on 2023-10-18 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Kurs')),
                ('name_uz', models.CharField(max_length=50, null=True, verbose_name='Kurs')),
                ('name_en', models.CharField(max_length=50, null=True, verbose_name='Kurs')),
                ('name_ru', models.CharField(max_length=50, null=True, verbose_name='Kurs')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nomi')),
                ('name_uz', models.CharField(max_length=50, null=True, verbose_name='Nomi')),
                ('name_en', models.CharField(max_length=50, null=True, verbose_name='Nomi')),
                ('name_ru', models.CharField(max_length=50, null=True, verbose_name='Nomi')),
                ('sub_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('content_uz', models.TextField(null=True, verbose_name='Content')),
                ('content_en', models.TextField(null=True, verbose_name='Content')),
                ('content_ru', models.TextField(null=True, verbose_name='Content')),
                ('image', models.ImageField(default='./news/news.png', upload_to='./news/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('upload_at', models.DateTimeField(auto_now=True)),
                ('sees', models.IntegerField(default=65)),
            ],
        ),
        migrations.CreateModel(
            name='StudentTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='./jadval/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='./requirements/')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='./description/')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='./oquv/')),
                ('course', models.ManyToManyField(to='main.course')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='CourseShip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.curriculum')),
            ],
        ),
    ]
