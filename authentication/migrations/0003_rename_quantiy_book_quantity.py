# Generated by Django 4.2.2 on 2023-06-10 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_book_isbn_book_quantiy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='quantiy',
            new_name='quantity',
        ),
    ]