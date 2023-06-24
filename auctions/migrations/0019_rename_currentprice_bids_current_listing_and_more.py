# Generated by Django 4.1.7 on 2023-06-03 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_alter_listings_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bids',
            old_name='currentPrice',
            new_name='current_listing',
        ),
        migrations.AddField(
            model_name='bids',
            name='listing_bid',
            field=models.IntegerField(default=0),
        ),
    ]