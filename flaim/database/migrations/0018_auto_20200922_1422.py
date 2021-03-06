# Generated by Django 3.0.7 on 2020-09-22 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0017_categoryproductcodemappingsupport_verified_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenceCategorySupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=500)),
                ('subcategory_id', models.CharField(max_length=50)),
                ('subcategory', models.CharField(max_length=500)),
                ('reference_amount', models.FloatField(blank=True, null=True)),
                ('reference_amount_units', models.CharField(blank=True, max_length=50, null=True)),
                ('reference_amount_extra', models.CharField(blank=True, max_length=50, null=True)),
                ('reference_amount_raw', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ReferenceSubcategorySupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_id', models.CharField(max_length=50)),
                ('subcategory', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SubcategorySupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='historicalproduct',
            name='atwater_test_pass',
        ),
        migrations.RemoveField(
            model_name='product',
            name='atwater_test_pass',
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='atwater_result',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='atwater_result',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='categoryproductcodemappingsupport',
            name='category',
            field=models.CharField(choices=[('Baby Food', 'Baby Food'), ('Bakery Products', 'Bakery Products'), ('Beverages', 'Beverages'), ('Cereals and Other Grain Products', 'Cereals and Other Grain Products'), ('Combination Dishes', 'Combination Dishes'), ('Dairy Products and Substitutes', 'Dairy Products and Substitutes'), ('Desserts', 'Desserts'), ('Dessert Toppings and Fillings', 'Dessert Toppings and Fillings'), ('Eggs and Egg Substitutes', 'Eggs and Egg Substitutes'), ('Fats and Oils', 'Fats and Oils'), ('Fruit and Fruit Juices', 'Fruit and Fruit Juices'), ('Legumes', 'Legumes'), ('Marine and Fresh Water Animals', 'Marine and Fresh Water Animals'), ('Meal Replacements and Supplements', 'Meal Replacements and Supplements'), ('Meat and Poultry, Products and Substitutes', 'Meat and Poultry, Products and Substitutes'), ('Miscellaneous', 'Miscellaneous'), ('Nuts and Seeds', 'Nuts and Seeds'), ('Potatoes, Sweet Potatoes and Yams', 'Potatoes, Sweet Potatoes and Yams'), ('Salads', 'Salads'), ('Sauces, Dips, Gravies and Condiments', 'Sauces, Dips, Gravies and Condiments'), ('Snacks', 'Snacks'), ('Soups', 'Soups'), ('Sugars and Sweets', 'Sugars and Sweets'), ('Vegetables', 'Vegetables'), ('Meal Replacements and Nutritional Supplements', 'Meal Replacements and Nutritional Supplements'), ('Not Food', 'Not Food'), ('Unknown', 'Unknown')], max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.Category'),
        ),
        migrations.CreateModel(
            name='ReferenceSubcategoryAmountSupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_amount', models.CharField(max_length=50)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.ReferenceCategorySupport')),
            ],
        ),
        migrations.CreateModel(
            name='AssignedSubcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('predicted_subcategory_1', models.CharField(blank=True, max_length=500, null=True)),
                ('confidence_1', models.FloatField(blank=True, null=True)),
                ('predicted_subcategory_2', models.CharField(blank=True, max_length=500, null=True)),
                ('confidence_2', models.FloatField(blank=True, null=True)),
                ('predicted_subcategory_3', models.CharField(blank=True, max_length=500, null=True)),
                ('confidence_3', models.FloatField(blank=True, null=True)),
                ('manual_subcategory', models.CharField(blank=True, max_length=500, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('model_version', models.CharField(blank=True, max_length=50, null=True)),
                ('parent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.ReferenceCategorySupport')),
                ('verified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Subcategory',
                'verbose_name_plural': 'Subcategories',
            },
        ),
    ]
