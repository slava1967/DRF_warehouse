# Generated by Django 4.2.10 on 2024-03-02 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
