# Generated by Django 3.0.7 on 2020-11-02 20:37

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0028_auto_20201007_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryproductcodemappingsupport',
            name='category',
            field=models.CharField(choices=[('Bakery Products', 'Bakery Products'), ('Beverages', 'Beverages'), ('Cereals and Other Grain Products', 'Cereals and Other Grain Products'), ('Dairy Products and Substitutes', 'Dairy Products and Substitutes'), ('Desserts', 'Desserts'), ('Dessert Toppings and Fillings', 'Dessert Toppings and Fillings'), ('Eggs and Egg Substitutes', 'Eggs and Egg Substitutes'), ('Fats and Oils', 'Fats and Oils'), ('Marine and Fresh Water Animals', 'Marine and Fresh Water Animals'), ('Fruit and Fruit Juices', 'Fruit and Fruit Juices'), ('Legumes', 'Legumes'), ('Meat and Poultry, Products and Substitutes', 'Meat and Poultry, Products and Substitutes'), ('Miscellaneous Category', 'Miscellaneous Category'), ('Combination Dishes', 'Combination Dishes'), ('Nuts and Seeds', 'Nuts and Seeds'), ('Potatoes, Sweet Potatoes and Yams', 'Potatoes, Sweet Potatoes and Yams'), ('Salads', 'Salads'), ('Sauces, Dips, Gravies and Condiments', 'Sauces, Dips, Gravies and Condiments'), ('Snacks', 'Snacks'), ('Soups', 'Soups'), ('Sugars and Sweets', 'Sugars and Sweets'), ('Vegetables', 'Vegetables'), ('Baby Food', 'Baby Food'), ('Meal Replacements and Nutritional Supplements', 'Meal Replacements and Nutritional Supplements'), ('Not Food', 'Not Food'), ('Unknown', 'Unknown')], max_length=500),
        ),
        migrations.AlterField(
            model_name='categoryproductcodemappingsupport',
            name='subcategory',
            field=models.CharField(blank=True, choices=[('Bread', 'Bread'), ('Bun, tortilla, pita', 'Bun, tortilla, pita'), ('Bagel, naan, flatbread', 'Bagel, naan, flatbread'), ('Brownie, dessert square', 'Brownie, dessert square'), ('Heavy weight cake', 'Heavy weight cake'), ('Medium weight cake', 'Medium weight cake'), ('Light weight cake', 'Light weight cake'), ('Sweet roll, flaky pastry', 'Sweet roll, flaky pastry'), ('Muffin', 'Muffin'), ('Cookie', 'Cookie'), ('Accompaniment cracker', 'Accompaniment cracker'), ('Snack cracker', 'Snack cracker'), ('Dry bread', 'Dry bread'), ('Toaster pastry', 'Toaster pastry'), ('Ice cream cone', 'Ice cream cone'), ('Crouton', 'Crouton'), ('Pancake, waffle', 'Pancake, waffle'), ('Grain bar with filling or coating', 'Grain bar with filling or coating'), ('Grain bar without filling or coating', 'Grain bar without filling or coating'), ('Energy or protein bar', 'Energy or protein bar'), ('Rice cake, corn cake', 'Rice cake, corn cake'), ('Pie, tart', 'Pie, tart'), ('Pie crust', 'Pie crust'), ('Pizza crust', 'Pizza crust'), ('Taco shell (hard)', 'Taco shell (hard)'), ('Carbonated or non-carbonated beverage', 'Carbonated or non-carbonated beverage'), ('Alcoholic beverage', 'Alcoholic beverage'), ('Coffee', 'Coffee'), ('Tea (hot)', 'Tea (hot)'), ('Cocoa or chocolate beverage (hot)', 'Cocoa or chocolate beverage (hot)'), ('Breakfast cereal (hot)', 'Breakfast cereal (hot)'), ('Breakfast cereal (RTE) less than 20 g per 250 mL', 'Breakfast cereal (RTE) less than 20 g per 250 mL'), ('Breakfast cereal (RTE) 20 to 42 g per 250 mL', 'Breakfast cereal (RTE) 20 to 42 g per 250 mL'), ('Breakfast cereal (RTE) 43 g or more per 250 mL', 'Breakfast cereal (RTE) 43 g or more per 250 mL'), ('Bran, wheat germ, chia', 'Bran, wheat germ, chia'), ('Flour, cornmeal', 'Flour, cornmeal'), ('Rice or other grain', 'Rice or other grain'), ('Pasta without sauce', 'Pasta without sauce'), ('Pasta dry and RTE', 'Pasta dry and RTE'), ('Starch', 'Starch'), ('Stuffing', 'Stuffing'), ('Cheese, cheese spread', 'Cheese, cheese spread'), ('Cottage cheese', 'Cottage cheese'), ('Cheese as an ingredient', 'Cheese as an ingredient'), ('Hard cheese', 'Hard cheese'), ('Quark, fresh cheese', 'Quark, fresh cheese'), ('Cream liquid', 'Cream liquid'), ('Cream powder', 'Cream powder'), ('Cream aerosol or whipped', 'Cream aerosol or whipped'), ('Eggnog', 'Eggnog'), ('Milk evaporated or condensed', 'Milk evaporated or condensed'), ('Milk, buttermilk', 'Milk, buttermilk'), ('Fermented dairy drinks', 'Fermented dairy drinks'), ('Shakes', 'Shakes'), ('Sour cream', 'Sour cream'), ('Yogurt', 'Yogurt'), ('Ice cream in tub', 'Ice cream in tub'), ('Ice cream as cake, sandwich or cone', 'Ice cream as cake, sandwich or cone'), ('Ice cream as pop, bar or cup', 'Ice cream as pop, bar or cup'), ('Sundae', 'Sundae'), ('Custard, gelatin, pudding', 'Custard, gelatin, pudding'), ('Dessert topping', 'Dessert topping'), ('Frosting, icing', 'Frosting, icing'), ('Pie filling', 'Pie filling'), ('Egg mixture', 'Egg mixture'), ('Egg in shell, liquid or dried', 'Egg in shell, liquid or dried'), ('Egg substitute', 'Egg substitute'), ('Butter, margarine', 'Butter, margarine'), ('Vegetable oil', 'Vegetable oil'), ('Butter replacement (powder)', 'Butter replacement (powder)'), ('Salad dressing', 'Salad dressing'), ('Mayonnaise', 'Mayonnaise'), ('Oil spray', 'Oil spray'), ('Anchovy, caviar', 'Anchovy, caviar'), ('Marine or fresh water animal with sauce', 'Marine or fresh water animal with sauce'), ('Marine or fresh water animal without sauce', 'Marine or fresh water animal without sauce'), ('Marine or fresh water animal canned', 'Marine or fresh water animal canned'), ('Marine or fresh water animal smoked or pickled', 'Marine or fresh water animal smoked or pickled'), ('Fruit fresh, frozen or canned', 'Fruit fresh, frozen or canned'), ('Blueberry, raspberry, blackberry', 'Blueberry, raspberry, blackberry'), ('Watermelon, cantaloupe, honeydew', 'Watermelon, cantaloupe, honeydew'), ('Avocado', 'Avocado'), ('Cranberry, lemon, lime', 'Cranberry, lemon, lime'), ('Apple sauce', 'Apple sauce'), ('Dried fruit', 'Dried fruit'), ('Candied or pickled fruit', 'Candied or pickled fruit'), ('Fruit for garnish', 'Fruit for garnish'), ('Fruit relish', 'Fruit relish'), ('Juice, juice substitute', 'Juice, juice substitute'), ('Juice as ingredient', 'Juice as ingredient'), ('Tofu, tempeh', 'Tofu, tempeh'), ('Bean, pea, lentil', 'Bean, pea, lentil'), ('Pork rind or bacon', 'Pork rind or bacon'), ('Beef, pork or poultry breakfast strip', 'Beef, pork or poultry breakfast strip'), ('Dried meat or poultry', 'Dried meat or poultry'), ('Luncheon meat', 'Luncheon meat'), ('Sausage', 'Sausage'), ('Meat or poultry without sauce', 'Meat or poultry without sauce'), ('Patty, cutlet, ground meat', 'Patty, cutlet, ground meat'), ('Meat or poultry, cured, smoked or pickled', 'Meat or poultry, cured, smoked or pickled'), ('Canned meat or poultry', 'Canned meat or poultry'), ('Meat or poultry with sauce', 'Meat or poultry with sauce'), ('Baking powder or soda, pectin, yeast', 'Baking powder or soda, pectin, yeast'), ('Baking decoration', 'Baking decoration'), ('Breadcrumb, batter mix', 'Breadcrumb, batter mix'), ('Cooking wine', 'Cooking wine'), ('Cocoa or carob powder', 'Cocoa or carob powder'), ('Non-alcoholic drink mixer ', 'Non-alcoholic drink mixer '), ('Chewing gum', 'Chewing gum'), ('Salad or potato topper', 'Salad or potato topper'), ('Salt, salt substitute, seasoning with salt', 'Salt, salt substitute, seasoning with salt'), ('Spice or herb without salt', 'Spice or herb without salt'), ('Coconut milk', 'Coconut milk'), ('Dried coconut flakes or shredded', 'Dried coconut flakes or shredded'), ('Combination dish measurable with a cup', 'Combination dish measurable with a cup'), ('Combination dish not measurable with a cup', 'Combination dish not measurable with a cup'), ("Hors d'oeurve", "Hors d'oeurve"), ('Nut or seed not for snacking', 'Nut or seed not for snacking'), ('Nut paste or cream', 'Nut paste or cream'), ('Peanut or nut butter', 'Peanut or nut butter'), ('Nut flour', 'Nut flour'), ('French fries, fried potato', 'French fries, fried potato'), ('Potato mashed, stuffed or with sauce', 'Potato mashed, stuffed or with sauce'), ('Potato plain, fresh, canned or frozen', 'Potato plain, fresh, canned or frozen'), ('Salad with egg, meat, fish, vegetable', 'Salad with egg, meat, fish, vegetable'), ('Gelatin salad', 'Gelatin salad'), ('Pasta or potato salad', 'Pasta or potato salad'), ('Sauce for dipping', 'Sauce for dipping'), ('Dip or spread with vegetable, legume or dairy', 'Dip or spread with vegetable, legume or dairy'), ('Major main entrée sauce', 'Major main entrée sauce'), ('Minor main entrée sauce', 'Minor main entrée sauce'), ('Major condiment', 'Major condiment'), ('Minor condiment', 'Minor condiment'), ('Chip, popcorn or snack with grain, pulse or fruit', 'Chip, popcorn or snack with grain, pulse or fruit'), ('Nut or seed for snacking', 'Nut or seed for snacking'), ('Meat or poultry stick for snacking', 'Meat or poultry stick for snacking'), ('All varieties of soup', 'All varieties of soup'), ('Candy, chocolate', 'Candy, chocolate'), ('After-dinner confection ', 'After-dinner confection '), ('Hard, powder or liquid candy', 'Hard, powder or liquid candy'), ('Baking candy', 'Baking candy'), ('Breath mint', 'Breath mint'), ('Roll-type or hard candy in dispenser package', 'Roll-type or hard candy in dispenser package'), ("Confectioner's or icing sugar", "Confectioner's or icing sugar"), ('Honey, molasses, bread spread', 'Honey, molasses, bread spread'), ('Jam, jelly, marmalade', 'Jam, jelly, marmalade'), ('Fruit leather', 'Fruit leather'), ('Marshmallow', 'Marshmallow'), ('Sugar', 'Sugar'), ('Sugar substitute', 'Sugar substitute'), ('Syrup as a topping', 'Syrup as a topping'), ('Syrup as an ingredient', 'Syrup as an ingredient'), ('Vegetable without sauce', 'Vegetable without sauce'), ('Vegetable with sauce', 'Vegetable with sauce'), ('Vegetable for garnish', 'Vegetable for garnish'), ('Chili pepper, green onion', 'Chili pepper, green onion'), ('Seaweed, dried mushroom', 'Seaweed, dried mushroom'), ('Sprout', 'Sprout'), ('Vegetable juice or drink', 'Vegetable juice or drink'), ('Olive', 'Olive'), ('Vegetable in oil, pickle', 'Vegetable in oil, pickle'), ('Relish', 'Relish'), ('Vegetable paste', 'Vegetable paste'), ('Vegetable sauce or purée', 'Vegetable sauce or purée'), ('Cereal dry or instant', 'Cereal dry or instant'), ('RTE cereal, cereal bar', 'RTE cereal, cereal bar'), ('Cookie, puff, yogurt melt', 'Cookie, puff, yogurt melt'), ('Strained or junior meat, fruit or vegetable', 'Strained or junior meat, fruit or vegetable'), ('Combination dish (one to under four years of age)', 'Combination dish (one to under four years of age)'), ('All varieties of juice', 'All varieties of juice'), ('Yogurt (one to under four years of age)', 'Yogurt (one to under four years of age)'), ('Meal replacement, nutritional supplement', 'Meal replacement, nutritional supplement'), ('Not Food', 'Not Food'), ('Unknown', 'Unknown')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproduct',
            name='store',
            field=models.CharField(choices=[('LOBLAWS', 'Loblaws'), ('WALMART', 'Walmart'), ('VOILA', 'Voila'), ('GROCERYGATEWAY', 'Grocery Gateway'), ('AMAZON', 'Amazon')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='store',
            field=models.CharField(choices=[('LOBLAWS', 'Loblaws'), ('WALMART', 'Walmart'), ('VOILA', 'Voila'), ('GROCERYGATEWAY', 'Grocery Gateway'), ('AMAZON', 'Amazon')], max_length=50),
        ),
        migrations.CreateModel(
            name='VoilaProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('image_directory', models.CharField(blank=True, max_length=500, null=True)),
                ('sku', models.CharField(blank=True, max_length=50, null=True)),
                ('bullets', models.TextField(blank=True, null=True)),
                ('dietary_info', models.TextField(blank=True, null=True)),
                ('nutrition_facts_json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='voila_product', to='database.Product')),
            ],
            options={
                'verbose_name': 'Voila Product',
                'verbose_name_plural': 'Voila Products',
            },
        ),
        migrations.CreateModel(
            name='HistoricalVoilaProduct',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('image_directory', models.CharField(blank=True, max_length=500, null=True)),
                ('sku', models.CharField(blank=True, max_length=50, null=True)),
                ('bullets', models.TextField(blank=True, null=True)),
                ('dietary_info', models.TextField(blank=True, null=True)),
                ('nutrition_facts_json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='database.Product')),
            ],
            options={
                'verbose_name': 'historical Voila Product',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalGroceryGatewayProduct',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('image_directory', models.CharField(blank=True, max_length=500, null=True)),
                ('sku', models.CharField(blank=True, max_length=50, null=True)),
                ('bullets', models.TextField(blank=True, null=True)),
                ('dietary_info', models.TextField(blank=True, null=True)),
                ('nutrition_facts_json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='database.Product')),
            ],
            options={
                'verbose_name': 'historical Grocery Gateway Product',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='GroceryGatewayProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('image_directory', models.CharField(blank=True, max_length=500, null=True)),
                ('sku', models.CharField(blank=True, max_length=50, null=True)),
                ('bullets', models.TextField(blank=True, null=True)),
                ('dietary_info', models.TextField(blank=True, null=True)),
                ('nutrition_facts_json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='grocerygateway_product', to='database.Product')),
            ],
            options={
                'verbose_name': 'Grocery Gateway Product',
                'verbose_name_plural': 'Grocery Gateway Products',
            },
        ),
        migrations.AddIndex(
            model_name='voilaproduct',
            index=models.Index(fields=['product'], name='database_vo_product_183a0f_idx'),
        ),
        migrations.AddIndex(
            model_name='grocerygatewayproduct',
            index=models.Index(fields=['product'], name='database_gr_product_6bf30d_idx'),
        ),
    ]
