# Generated by Django 2.2.8 on 2019-12-04 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attributevariants',
            old_name='variant_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='attributevariants',
            old_name='variant_option',
            new_name='type',
        ),
        migrations.AddField(
            model_name='attributevariants',
            name='price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10, max_length=32),
        ),
    ]