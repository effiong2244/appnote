# Generated by Django 4.2 on 2023-06-29 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appnote1', '0003_tag_order_customer_order_product_product_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
