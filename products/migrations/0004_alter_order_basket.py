# Generated by Django 4.2.5 on 2024-01-16 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.basket'),
        ),
    ]
