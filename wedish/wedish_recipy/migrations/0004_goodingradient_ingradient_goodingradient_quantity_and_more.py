# Generated by Django 4.0.4 on 2022-04-20 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wedish_store', '0001_initial'),
        ('wedish_recipy', '0003_goodingradient'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodingradient',
            name='ingradient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='wedish_store.product', verbose_name='ingredient'),
        ),
        migrations.AddField(
            model_name='goodingradient',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='quantity'),
        ),
        migrations.AddField(
            model_name='goodingradient',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='wedish_store.unit', verbose_name='unit'),
        ),
    ]
