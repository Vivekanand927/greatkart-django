# Generated by Django 3.1 on 2022-03-21 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_cartitem_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='variation',
            new_name='variations',
        ),
    ]