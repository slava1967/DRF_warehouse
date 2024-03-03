# Generated by Django 4.2.10 on 2024-03-02 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_order_warehouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='warehouse',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='api.warehouse'),
            preserve_default=False,
        ),
    ]