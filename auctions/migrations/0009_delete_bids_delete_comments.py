# Generated by Django 4.1.7 on 2023-05-09 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_remove_listings_creater'),
    ]

    operations = [
        migrations.DeleteModel(
            name='bids',
        ),
        migrations.DeleteModel(
            name='comments',
        ),
    ]
