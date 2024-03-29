# Generated by Django 3.2.9 on 2022-08-04 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0002_restaurant_menus'),
        ('client', '0001_initial'),
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_value', models.FloatField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_client', to='client.client')),
                ('items', models.ManyToManyField(blank=True, related_name='order_items', to='item.Item')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_restaurant', to='restaurant.restaurant')),
            ],
        ),
    ]
