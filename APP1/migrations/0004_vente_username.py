# Generated by Django 4.2.1 on 2023-06-29 01:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APP1', '0003_alter_produit_nom_produit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vente',
            name='username',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
