# Generated by Django 4.1.2 on 2023-04-11 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0009_alter_question_options_remove_lesson_num_lesson_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='poll.teacher'),
        ),
    ]
