# Generated by Django 3.0.1 on 2020-01-04 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perform', '0002_auto_20200104_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback_setting',
            name='feed_type',
            field=models.CharField(choices=[('one', 'Reporting To'), ('two', 'Peer-To-Peer'), ('three', '360-Degree')], default='one', max_length=20),
        ),
    ]
