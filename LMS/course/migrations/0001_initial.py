# Generated by Django 4.2.7 on 2023-11-27 14:34

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='course.basemodel')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('cover_image', models.FileField(upload_to='')),
                ('duration', models.DurationField()),
                ('lang', models.CharField(choices=[('EN', 'English'), ('AR', 'Arabic'), ('FR', 'French')], default='AR', max_length=2)),
            ],
            bases=('course.basemodel',),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=245, unique=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='course.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='course.basemodel')),
                ('title', models.CharField(max_length=245)),
                ('content', models.TextField()),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
            bases=('course.basemodel',),
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='course.category'),
        ),
    ]
