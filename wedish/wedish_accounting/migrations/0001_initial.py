
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wedish_pub', '0001_initial'),
        ('cities_light', '0011_alter_city_country_alter_city_id_alter_city_region_and_more'),
        ('wedish_menu', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wedish_menu', '0001_initial'),
    ]
    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimated_to_complete', models.DateTimeField(blank=True, null=True, verbose_name='Estimated to complete')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Price')),
                ('completed_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='completed_at')),
                ('table_number', models.CharField(db_index=True, max_length=100, verbose_name='Table number')),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Spaces', to='wedish_pub.space', verbose_name='Space')),
                ('server', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_for_staff', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_for_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ['table_number', 'server', 'estimated_to_complete'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(db_index=True, max_length=100, verbose_name='Payment method')),
                ('currency', models.CharField(db_index=True, max_length=10, verbose_name='Currency')),
            ],
        ),
        migrations.CreateModel(
            name='VAT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Rate')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Start date')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End date')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.country')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=100, verbose_name='Quantity')),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Total price')),
                ('menu_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='wedish_menu.menuitem', verbose_name='Menu item')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='places', to='wedish_accounting.order', verbose_name='Order')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Total price')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Discount')),
                ('tips', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Tips')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='wedish_accounting.order', verbose_name='Order')),
            ],
        ),
    ]
