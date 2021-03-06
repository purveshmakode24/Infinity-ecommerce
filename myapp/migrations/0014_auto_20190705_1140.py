# Generated by Django 2.2.2 on 2019-07-05 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20190705_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='entry_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_user_cart', to=settings.AUTH_USER_MODEL),
        ),
    ]
