# Generated by Django 4.2.2 on 2023-06-12 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_book_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='issued',
            field=models.IntegerField(default=0),
        ),
    ]
