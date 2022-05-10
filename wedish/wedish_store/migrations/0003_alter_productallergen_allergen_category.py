# Generated by Django 4.0.4 on 2022-05-06 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedish_store', '0002_alter_product_options_alter_productallergen_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productallergen',
            name='allergen_category',
            field=models.CharField(choices=[('none', 'none'), ('celery', 'celery'), ('gluten', 'cereals containing gluten'), ('crustaceans', 'crustaceans'), ('eggs', 'eggs'), ('fish', 'fish'), ('lupin', 'lupin'), ('milk', 'milk'), ('molluscs', 'molluscs'), ('mustard', 'mustard'), ('peanuts', 'peanuts'), ('sesame', 'sesame'), ('soybeans', 'soybeans'), ('SO', 'sulphur dioxide and sulpites > 10 ppm'), ('tree nuts', 'tree nuts')], db_index=True, max_length=63),
        ),
    ]
