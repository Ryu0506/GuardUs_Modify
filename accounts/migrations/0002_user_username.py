# Generated by Django 3.0.9 on 2020-08-20 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='electricray', max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
