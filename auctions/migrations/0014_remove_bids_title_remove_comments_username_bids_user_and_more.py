# Generated by Django 4.1.7 on 2023-05-17 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_listings_creater'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bids',
            name='title',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='username',
        ),
        migrations.AddField(
            model_name='bids',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='creater',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='userID', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='listings',
            name='category',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AddField(
            model_name='listings',
            name='comment',
            field=models.ManyToManyField(blank=True, related_name='comments', to='auctions.comments'),
        ),
        migrations.AlterField(
            model_name='bids',
            name='currentPrice',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bid', to='auctions.listings'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='creater',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='created_listings', to=settings.AUTH_USER_MODEL),
        ),
    ]
