# Generated by Django 3.1.3 on 2020-11-19 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_product_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='user_id',
            new_name='user_ids',
        ),
    ]
