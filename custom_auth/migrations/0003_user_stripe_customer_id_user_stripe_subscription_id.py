# Generated by Django 4.2.2 on 2023-07-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0002_user_expired_at_user_is_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Stripe(CusID)'),
        ),
        migrations.AddField(
            model_name='user',
            name='stripe_subscription_id',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Stripe(SubID)'),
        ),
    ]
