# Generated by Django 3.0.4 on 2020-03-24 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('available_stock', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('birth_date', models.DateField(null=True)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(max_length=15)),
                ('fidelity_points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('NEW', 'New Order'), ('PAID', 'Paid Order')], default='NEW', max_length=32)),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookshop.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderBookQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshop.Book')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchased_books', to='bookshop.Order')),
            ],
        ),
        migrations.AddConstraint(
            model_name='genre',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_genre_name_constraint'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookshop.Genre'),
        ),
        migrations.AddConstraint(
            model_name='orderbookquantity',
            constraint=models.UniqueConstraint(fields=('id', 'order', 'book'), name='unique_book_by_order_constraint'),
        ),
    ]
