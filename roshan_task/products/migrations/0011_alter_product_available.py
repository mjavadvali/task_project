# Generated by Django 5.1.3 on 2024-11-27 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
