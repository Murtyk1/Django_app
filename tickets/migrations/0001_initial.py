# Generated by Django 5.2.1 on 2025-05-30 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=3, verbose_name='Откуда (IATA код)')),
                ('destination', models.CharField(max_length=3, verbose_name='Куда (IATA код)')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('departure_date', models.DateField(verbose_name='Дата вылета')),
                ('airline', models.CharField(max_length=50, verbose_name='Авиакомпания')),
            ],
        ),
    ]
