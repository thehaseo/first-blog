# Generated by Django 4.0.3 on 2022-03-09 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(db_index=True, default='', max_length=100),
        ),
    ]
