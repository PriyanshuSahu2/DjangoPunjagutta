# Generated by Django 5.0.4 on 2024-05-04 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='Name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='AGe'),
        ),
        migrations.AddField(
            model_name='student',
            name='roll_number',
            field=models.PositiveIntegerField(default=0, primary_key=True, serialize=False, verbose_name='Roll Number'),
        ),
    ]
