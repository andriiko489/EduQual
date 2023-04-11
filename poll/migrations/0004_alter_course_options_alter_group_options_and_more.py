# Generated by Django 4.1.2 on 2023-04-11 19:27

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('poll', '0003_question_teacherlectureassessment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Group', 'verbose_name_plural': 'Groups'},
        ),
        migrations.AlterModelOptions(
            name='institute',
            options={'verbose_name': 'Institute', 'verbose_name_plural': 'Institutes'},
        ),
        migrations.AlterModelOptions(
            name='specialization',
            options={'verbose_name': 'Specialization', 'verbose_name_plural': 'Specializations'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Subject', 'verbose_name_plural': 'Subjects'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Teacher', 'verbose_name_plural': 'Teachers'},
        ),
        migrations.AlterModelOptions(
            name='university',
            options={'verbose_name': 'University', 'verbose_name_plural': 'Universities'},
        ),
        migrations.RemoveField(
            model_name='university',
            name='domen',
        ),
        migrations.AddField(
            model_name='teacherlectureassessment',
            name='actuality',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='teacherlectureassessment',
            name='average',
            field=models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=6),
        ),
        migrations.AddField(
            model_name='teacherlectureassessment',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='teacherlectureassessment',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teacherlectureassessment',
            name='informative',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='teacherlectureassessment',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacherlectureassessment',
            name='total',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='university',
            name='domain',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='institute',
            unique_together={('name', 'university')},
        ),
        migrations.AlterUniqueTogether(
            name='specialization',
            unique_together={('name', 'institute')},
        ),
        migrations.AlterUniqueTogether(
            name='teacherlectureassessment',
            unique_together={('content_type', 'object_id')},
        ),
    ]
