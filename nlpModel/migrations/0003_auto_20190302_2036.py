# Generated by Django 2.1.7 on 2019-03-03 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nlpModel', '0002_auto_20190302_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nlpmodel',
            old_name='description',
            new_name='question',
        ),
        migrations.RemoveField(
            model_name='nlpmodel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='nlpmodel',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='nlpmodel',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='nlpmodel',
            name='title',
        ),
    ]
