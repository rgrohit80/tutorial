# Generated by Django 2.1.7 on 2019-06-15 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0004_auto_20190615_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_num',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
