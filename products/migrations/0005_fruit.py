# Generated by Django 5.0.2 on 2024-02-20 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_offer_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]