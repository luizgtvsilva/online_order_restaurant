# Generated by Django 3.2.9 on 2022-08-04 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('items_menu', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='items_menu', to='item.item')),
            ],
        ),
    ]