# Generated by Django 3.1.3 on 2020-11-10 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20201110_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='nutriscore_grad',
            new_name='nutriscore_grade',
        ),
    ]