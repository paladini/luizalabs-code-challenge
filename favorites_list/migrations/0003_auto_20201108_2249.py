# Generated by Django 3.1.3 on 2020-11-08 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('favorites_list', '0002_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='reviewScore',
            new_name='review_score',
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(db_index=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.CreateModel(
            name='FavoriteList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='favorites_list.client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='favorites_list.product')),
            ],
            options={
                'db_table': 'favorites_list',
                'unique_together': {('client', 'product')},
            },
        ),
        migrations.AddField(
            model_name='client',
            name='favorites',
            field=models.ManyToManyField(through='favorites_list.FavoriteList', to='favorites_list.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='favorited',
            field=models.ManyToManyField(through='favorites_list.FavoriteList', to='favorites_list.Client'),
        ),
    ]