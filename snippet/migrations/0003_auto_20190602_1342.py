# Generated by Django 2.1.7 on 2019-06-02 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0002_emp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('paradigm', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='emp',
            name='sal',
            field=models.IntegerField(),
        ),
    ]
