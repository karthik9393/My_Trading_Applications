# Generated by Django 5.0.6 on 2024-06-14 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TradeOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=10)),
                ('quantity', models.IntegerField(default=100)),
                ('order_type', models.CharField(default='Market', max_length=10)),
                ('algo_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('trade_action', models.CharField(max_length=4)),
                ('stop_loss_percentage', models.DecimalField(decimal_places=2, default=-1.0, max_digits=3)),
                ('timeframe', models.CharField(max_length=50)),
                ('executed', models.BooleanField(default=False)),
            ],
        ),
    ]
