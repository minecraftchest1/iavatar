# Generated by Django 2.1.3 on 2018-12-03 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivataraccount', '0012_auto_20181107_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreference',
            name='theme',
            field=models.CharField(choices=[('default', 'Default theme'), ('clime', 'climes theme'), ('green', 'green theme'), ('red', 'red theme')], default='default', max_length=10),
        ),
    ]
