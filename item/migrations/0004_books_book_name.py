# Generated by Django 3.2.10 on 2023-08-09 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_alter_books_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='Book_Name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]