# Generated by Django 4.1.1 on 2022-09-30 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=100000)),
                ('stock_amount', models.IntegerField()),
                ('price_value', models.IntegerField()),
                ('description', models.TextField()),
                ('bought_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]