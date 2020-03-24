# Generated by Django 3.0.4 on 2020-03-24 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0004_auto_20200324_0523'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'New Order'), ('paid', 'Paid')], default='new', max_length=32),
        ),
    ]
