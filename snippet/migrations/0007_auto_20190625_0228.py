# Generated by Django 2.1.7 on 2019-06-24 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0006_actor_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='snippet.Actor'),
        ),
    ]
