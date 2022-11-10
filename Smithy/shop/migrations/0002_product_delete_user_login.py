# Generated by Django 4.1.2 on 2022-11-10 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('T', 'Tools'), ('A', 'Agriculture'), ('W', 'Weapones'), ('U', 'Utensils')], max_length=1)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
        migrations.DeleteModel(
            name='user_login',
        ),
    ]
