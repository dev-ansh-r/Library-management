# Generated by Django 4.2.2 on 2023-06-12 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_rename_quantiy_book_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=False),
        ),
    ]
