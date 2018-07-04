# Generated by Django 2.0.6 on 2018-07-02 06:16

from django.db import migrations, models
import django.db.models.deletion
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_task_taskstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskstatus',
            name='commment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='taskstatus',
            name='response',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='taskstatus',
            name='state',
            field=django_fsm.FSMField(choices=[('PRC', 'process'), ('RVW', 'review'), ('DBT', 'debt'), ('CMP', 'complete')], default='PRC', max_length=50, protected=True),
        ),
        migrations.AlterField(
            model_name='taskstatus',
            name='task',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to='courses.Task', unique=True),
        ),
    ]