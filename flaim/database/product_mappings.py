PRODUCT_STORES = [
    'Loblaws',
    'Walmart',
    # 'Voila',
    # 'Grocery Gateway'
]

# All available categories that can be selected/predicted for any particular product. This list should be maintained.
# https://www.canada.ca/en/health-canada/services/technical-documents-labelling-requirements/table-reference-amounts-food.html
PRODUCT_CATEGORIES = [
    "Baby Food",
    "Bakery Products",
    "Beverages",
    "Cereals and Other Grain Products",
    "Combination Dishes",
    "Dairy Products and Substitutes",
    "Desserts",
    "Dessert Toppings and Fillings",
    "Eggs and Egg Substitutes",
    "Fats and Oils",
    "Fruit and Fruit Juices",
    "Legumes",
    "Marine and Fresh Water Animals",
    "Meal Replacements and Supplements",
    "Meat and Poultry, Products and Substitutes",
    "Miscellaneous",
    "Nuts and Seeds",
    "Potatoes, Sweet Potatoes and Yams",
    "Salads",
    "Sauces, Dips, Gravies and Condiments",
    "Snacks",
    "Soups",
    "Sugars and Sweets",
    "Vegetables",
    "Not Food",
    "Unknown"
]

# TODO: Use this instead of the PRODUCT_CATEGORIES list. This properly displays all categories and their respective
#  sub-categories.
REFERENCE_CATEGORIES_DICT = {
    'Bakery Products':
        ['Rice cake, corn cake', 'Pancake, waffle', 'Pizza crust', 'Bagel, naan, flatbread', 'Crouton',
         'Accompaniment cracker', 'Energy or protein bar', 'Medium weight cake',
         'Sweet roll, flaky pastry', 'Muffin', 'Ice cream cone', 'Pie crust', 'Toaster pastry',
         'Taco shell (hard)', 'Cookie', 'Heavy weight cake', 'Bread',
         'Grain bar without filling or coating', 'Light weight cake', 'Bun, tortilla, pita',
         'Snack cracker', 'Pie, tart', 'Dry bread', 'Brownie, dessert square',
         'Grain bar with filling or coating'],
    'Beverages':
        ['Coffee', 'Alcoholic beverage', 'Tea (hot)', 'Cocoa or chocolate beverage (hot)',
         'Carbonated or non-carbonated beverage'],
    'Cereals and Other Grain Products':
        ['Pasta without sauce', 'Flour, cornmeal', 'Pasta dry and RTE',
         'Breakfast cereal (RTE) less than 20 g per 250 mL', 'Stuffing',
         'Rice or other grain', 'Breakfast cereal (RTE) 20 to 42 g per 250 mL',
         'Breakfast cereal (RTE) 43 g or more per 250 mL', 'Starch',
         'Bran, wheat germ, chia', 'Breakfast cereal (hot)'],
    'Dairy Products and Substitutes':
        ['Fermented dairy drinks', 'Quark, fresh cheese', 'Cream powder', 'Hard cheese',
         'Yogurt', 'Cheese, cheese spread', 'Eggnog', 'Milk evaporated or condensed',
         'Cottage cheese', 'Sour cream', 'Cheese as an ingredient', 'Cream liquid',
         'Shakes', 'Cream aerosol or whipped', 'Milk, buttermilk'],
    'Desserts':
        ['Ice cream as cake, sandwich or cone', 'Ice cream in tub', 'Custard, gelatin, pudding',
         'Ice cream as pop, bar or cup', 'Sundae'],
    'Eggs and Egg Substitutes':
        ['Egg substitute', 'Egg in shell, liquid or dried', 'Egg mixture'],
    'Fats and Oils':
        ['Vegetable oil', 'Butter replacement (powder)', 'Oil spray', 'Mayonnaise', 'Salad dressing',
         'Butter, margarine'],
    'Marine and Fresh Water Animals':
        ['Anchovy, caviar', 'Marine or fresh water animal smoked or pickled',
         'Marine or fresh water animal with sauce', 'Marine or fresh water animal canned',
         'Marine or fresh water animal without sauce'],
    'Fruit and Fruit Juices':
        ['Fruit relish', 'Fruit fresh, frozen or canned', 'Blueberry, raspberry, blackberry',
         'Fruit for garnish', 'Candied or pickled fruit', 'Cranberry, lemon, lime', 'Dried fruit',
         'Juice as ingredient', 'Apple sauce', 'Avocado', 'Watermelon, cantaloupe, honeydew',
         'Juice, juice substitute'],
    'Legumes':
        ['Bean, pea, lentil', 'Tofu, tempeh'],
    'Meat and Poultry, Products and Substitutes':
        ['Meat or poultry without sauce', 'Pork rind or bacon',
         'Meat or poultry, cured, smoked or pickled',
         'Patty, cutlet, ground meat',
         'Beef, pork or poultry breakfast strip', 'Luncheon meat',
         'Canned meat or poultry', 'Meat or poultry with sauce',
         'Dried meat or poultry', 'Sausage'],
    'Miscellaneous':
        [],
    'Combination Dishes':
        ['Combination dish not measurable with a cup', "Hors d'oeurve",
         'Combination dish measurable with a cup'],
    'Nuts and Seeds':
        ['Nut flour', 'Peanut or nut butter', 'Nut or seed not for snacking', 'Nut paste or cream'],
    'Potatoes, Sweet Potatoes and Yams':
        ['Potato plain, fresh, canned or frozen',
         'Potato mashed, stuffed or with sauce', 'French fries, fried potato'],
    'Salads':
        ['Pasta or potato salad', 'Gelatin salad', 'Salad with egg, meat, fish, vegetable'],
    'Sauces, Dips, Gravies and Condiments':
        ['Sauce for dipping', 'Major condiment', 'Minor condiment',
         'Minor main entrée sauce', 'Major main entrée sauce',
         'Dip or spread with vegetable, legume or dairy'],
    'Snacks':
        ['Nut or seed for snacking', 'Chip, popcorn or snack with grain, pulse or fruit',
         'Meat or poultry stick for snacking'],
    'Soups':
        ['All varieties of soup'],
    'Sugars and Sweets':
        ['Honey, molasses, bread spread', 'Breath mint', 'Jam, jelly, marmalade',
         'After-dinner confection', 'Syrup as a topping', 'Sugar', 'Marshmallow', 'Candy, chocolate',
         'Sugar substitute', 'Hard, powder or liquid candy', 'Baking candy',
         'Roll-type or hard candy in dispenser package', "Confectioner's or icing sugar",
         'Syrup as an ingredient', 'Fruit leather'],
    'Vegetables':
        ['Vegetable without sauce', 'Vegetable in oil, pickle', 'Seaweed, dried mushroom',
         'Vegetable juice or drink', 'Vegetable with sauce', 'Relish', 'Vegetable paste',
         'Chili pepper, green onion', 'Sprout', 'Vegetable sauce or purée', 'Vegetable for garnish', 'Olive'],
    'Baby Food':
        ['Yogurt (one to under four years of age)',
         'Cookie, puff, yogurt melt', 'RTE cereal, cereal bar',
         'Combination dish (one to under four years of age)',
         'Strained or junior meat, fruit or vegetable',
         'All varieties of juice', 'Cereal dry or instant'],
    'Meal Replacements and Nutritional Supplements':
        ['Meal replacement, nutritional supplement']
}

REFERENCE_CATEGORIES_CODING_DICT = {
    'A': 'Bakery Products',
    'B': 'Beverages',
    'C': 'Cereals and Other Grain Products',
    'D': 'Dairy Products and Substitutes',
    'E': 'Desserts',
    'F': 'Dessert Toppings and Fillings',
    'G': 'Eggs and Egg Substitutes',
    'H': 'Fats and Oils',
    'I': 'Marine and Fresh Water Animals',
    'J': 'Fruit and Fruit Juices',
    'K': 'Legumes',
    'L': 'Meat and Poultry, Products and Substitutes',
    'M': 'Miscellaneous Category',
    'N': 'Combination Dishes',
    'O': 'Nuts and Seeds',
    'P': 'Potatoes, Sweet Potatoes and Yams',
    'Q': 'Salads',
    'R': 'Sauces, Dips, Gravies and Condiments',
    'S': 'Snacks',
    'T': 'Soups',
    'U': 'Sugars and Sweets',
    'V': 'Vegetables',
    'W': 'Baby Food',
    'X': 'Meal Replacements and Nutritional Supplements'
}

REFERENCE_SUBCATEGORIES_CODING_DICT = {
    'A.1': 'Bread',
    'A.2': 'Bun, tortilla, pita',
    'A.3': 'Bagel, naan, flatbread',
    'A.4': 'Brownie, dessert square',
    'A.5': 'Heavy weight cake',
    'A.6': 'Medium weight cake',
    'A.7': 'Light weight cake',
    'A.8': 'Sweet roll, flaky pastry',
    'A.9': 'Muffin',
    'A.10': 'Cookie',
    'A.11': 'Accompaniment cracker',
    'A.12': 'Snack cracker',
    'A.13': 'Dry bread',
    'A.14': 'Toaster pastry',
    'A.15': 'Ice cream cone',
    'A.16': 'Crouton',
    'A.17': 'Pancake, waffle',
    'A.18': 'Grain bar with filling or coating',
    'A.19': 'Grain bar without filling or coating',
    'A.20': 'Energy or protein bar',
    'A.21': 'Rice cake, corn cake',
    'A.22': 'Pie, tart',
    'A.23': 'Pie crust',
    'A.24': 'Pizza crust',
    'A.25': 'Taco shell (hard)',
    'B.1': 'Carbonated or non-carbonated beverage ',
    'B.2': 'Alcoholic beverage',
    'B.3': 'Coffee',
    'B.4': 'Tea (hot)',
    'B.5': 'Cocoa or chocolate beverage (hot)',
    'C.1': 'Breakfast cereal (hot)',
    'C.2': 'Breakfast cereal (RTE) less than 20 g per 250 mL',
    'C.3': 'Breakfast cereal (RTE) 20 to 42 g per 250 mL',
    'C.4': 'Breakfast cereal (RTE) 43 g or more per 250 mL',
    'C.5': 'Bran, wheat germ, chia',
    'C.6': 'Flour, cornmeal',
    'C.7': 'Rice or other grain',
    'C.8': 'Pasta without sauce',
    'C.9': 'Pasta dry and RTE',
    'C.10': 'Starch',
    'C.11': 'Stuffing',
    'D.1': 'Cheese, cheese spread',
    'D.2': 'Cottage cheese',
    'D.3': 'Cheese as an ingredient',
    'D.4': 'Hard cheese',
    'D.5': 'Quark, fresh cheese',
    'D.6': 'Cream liquid',
    'D.7': 'Cream powder',
    'D.8': 'Cream aerosol or whipped',
    'D.9': 'Eggnog',
    'D.10': 'Milk evaporated or condensed',
    'D.11': 'Milk, buttermilk',
    'D.12': 'Fermented dairy drinks',
    'D.13': 'Shakes',
    'D.14': 'Sour cream',
    'D.15': 'Yogurt',
    'E.1': 'Ice cream in tub',
    'E.2': 'Ice cream as cake, sandwich or cone',
    'E.3': 'Ice cream as pop, bar or cup',
    'E.4': 'Sundae',
    'E.5': 'Custard, gelatin, pudding',
    'F.1': 'Dessert topping',
    'F.2': 'Frosting, icing',
    'F.3': 'Pie filling',
    'G.1': 'Egg mixture',
    'G.2': 'Egg in shell, liquid or dried',
    'G.3': 'Egg substitute',
    'H.1': 'Butter, margarine',
    'H.2': 'Vegetable oil',
    'H.3': 'Butter replacement (powder)',
    'H.4': 'Salad dressing',
    'H.5': 'Mayonnaise',
    'H.6': 'Oil spray',
    'I.1': 'Anchovy, caviar',
    'I.2': 'Marine or fresh water animal with sauce',
    'I.3': 'Marine or fresh water animal without sauce',
    'I.4': 'Marine or fresh water animal canned',
    'I.5': 'Marine or fresh water animal smoked or pickled',
    'J.1': 'Fruit fresh, frozen or canned',
    'J.2': 'Blueberry, raspberry, blackberry',
    'J.3': 'Watermelon, cantaloupe, honeydew',
    'J.4': 'Avocado',
    'J.5': 'Cranberry, lemon, lime',
    'J.6': 'Apple sauce',
    'J.7': 'Dried fruit',
    'J.8': 'Candied or pickled fruit',
    'J.9': 'Fruit for garnish',
    'J.10': 'Fruit relish',
    'J.11': 'Juice, juice substitute',
    'J.12': 'Juice as ingredient',
    'K.1': 'Tofu, tempeh',
    'K.2': 'Bean, pea, lentil',
    'L.1': 'Pork rind or bacon',
    'L.2': 'Beef, pork or poultry breakfast strip',
    'L.3': 'Dried meat or poultry',
    'L.4': 'Luncheon meat',
    'L.5': 'Sausage',
    'L.6': 'Meat or poultry without sauce',
    'L.7': 'Patty, cutlet, ground meat',
    'L.8': 'Meat or poultry, cured, smoked or pickled',
    'L.9': 'Canned meat or poultry',
    'L.10': 'Meat or poultry with sauce',
    'M.1': 'Baking powder or soda, pectin, yeast',
    'M.2': 'Baking decoration',
    'M.3': 'Breadcrumb, batter mix',
    'M.4': 'Cooking wine',
    'M.5': 'Cocoa or carob powder',
    'M.6': 'Non-alcoholic drink mixer ',
    'M.7': 'Chewing gum',
    'M.8': 'Salad or potato topper',
    'M.9': 'Salt, salt substitute, seasoning with salt',
    'M.10': 'Spice or herb without salt',
    'M.11': 'Coconut milk',
    'M.12': 'Dried coconut flakes or shredded',
    'N.1': 'Combination dish measurable with a cup',
    'N.2': 'Combination dish not measurable with a cup',
    'N.3': "Hors d'oeurve",
    'O.1': 'Nut or seed not for snacking',
    'O.2': 'Nut paste or cream',
    'O.3': 'Peanut or nut butter',
    'O.4': 'Nut flour',
    'P.1': 'French fries, fried potato',
    'P.2': 'Potato mashed, stuffed or with sauce',
    'P.3': 'Potato plain, fresh, canned or frozen',
    'Q.1': 'Salad with egg, meat, fish, vegetable',
    'Q.2': 'Gelatin salad',
    'Q.3': 'Pasta or potato salad',
    'R.1': 'Sauce for dipping',
    'R.2': 'Dip or spread with vegetable, legume or dairy',
    'R.3': 'Major main entrée sauce',
    'R.4': 'Minor main entrée sauce',
    'R.5': 'Major condiment',
    'R.6': 'Minor condiment',
    'S.1': 'Chip, popcorn or snack with grain, pulse or fruit',
    'S.2': 'Nut or seed for snacking',
    'S.3': 'Meat or poultry stick for snacking',
    'T.1': 'All varieties of soup',
    'U.1': 'Candy, chocolate',
    'U.2': 'After-dinner confection ',
    'U.3': 'Hard, powder or liquid candy',
    'U.4': 'Baking candy',
    'U.5': 'Breath mint',
    'U.6': 'Roll-type or hard candy in dispenser package',
    'U.7': "Confectioner's or icing sugar",
    'U.8': 'Honey, molasses, bread spread',
    'U.9': 'Jam, jelly, marmalade',
    'U.10': 'Fruit leather',
    'U.11': 'Marshmallow',
    'U.12': 'Sugar',
    'U.13': 'Sugar substitute',
    'U.14': 'Syrup as a topping',
    'U.15': 'Syrup as an ingredient',
    'V.1': 'Vegetable without sauce',
    'V.2': 'Vegetable with sauce',
    'V.3': 'Vegetable for garnish',
    'V.4': 'Chili pepper, green onion',
    'V.5': 'Seaweed, dried mushroom',
    'V.6': 'Sprout',
    'V.7': 'Vegetable juice or drink',
    'V.8': 'Olive',
    'V.9': 'Vegetable in oil, pickle',
    'V.10': 'Relish',
    'V.11': 'Vegetable paste',
    'V.12': 'Vegetable sauce or purée',
    'W.1': 'Cereal dry or instant',
    'W.2': 'RTE cereal, cereal bar',
    'W.3': 'Cookie, puff, yogurt melt',
    'W.4': 'Strained or junior meat, fruit or vegetable',
    'W.5': 'Combination dish (one to under four years of age)',
    'W.6': 'All varieties of juice',
    'W.7': 'Yogurt (one to under four years of age)',
    'X.1': 'Meal replacement, nutritional supplement'
}

FLIP_TO_FLAIME_CONVERSION_DICT = {
    'Product Name': 'name',
    'Ingredients': 'ingredients',
    'KCAL': 'calories',
    'FAT': 'totalfat',
    'FAT_%DV': 'totalfat_dv',
    'SATFAT': 'saturatedfat',
    'SATFAT_%DV': 'saturatedfat_dv',
    'TRANS': 'transfat',
    'CHOL': 'cholesterol',
    'NA': 'sodium',
    'NA_%DV': 'sodium_dv',
    'CHO': 'totalcarbohydrate_dv',
    'FIBRE': 'dietaryfiber',
    'SUGAR': 'sugar',
    'PRO': 'protein',
    'VITA%': 'vitamina_dv',
    'VITC%': 'vitaminc_dv',
    'CALCIUM%': 'calcium_dv',
    'IRON%': 'iron_dv'
}

VALID_NUTRIENT_DICT = {
    'calories': 'Calories',
    'sodium': 'Sodium',
    'sodium_dv': 'Sodium',
    'calcium': 'Calcium',
    'calcium_dv': 'Calcium',
    'totalfat': 'Total Fat',
    'totalfat_dv': 'Total Fat',
    'monounsaturated_fat': 'Monounsaturated Fat',
    'polyunsaturated_fat': 'Polyunsaturated Fat',
    'saturatedfat': 'Saturated Fat',
    'saturatedfat_dv': 'Saturated Fat',
    'omega3fattyacids': 'Omega 3',
    'transfat': 'Trans. Fat',
    'transfat_dv': 'Trans. Fat',
    'potassium': 'Potassium',
    'potassium_dv': 'Potassium',
    'totalcarbohydrate': 'Total Carbohydrate',
    'totalcarbohydrate_dv': 'Total Carbohydrate',
    'dietaryfiber': 'Dietary Fiber',
    'dietaryfiber_dv': 'Dietary Fiber',
    'sugar': 'Sugar',
    'protein': 'Protein',
    'cholesterol': 'Cholesterol',
    'vitamina': 'Vitamin A',
    'vitamina_dv': 'Vitamin A',
    'vitaminc': 'Vitamin C',
    'vitaminc_dv': 'Vitamin C',
    'vitamind': 'Vitamin D',
    'vitamine': 'Vitamin E',
    'niacin': 'Niacin',
    'vitaminb6': 'Vitamin B6',
    'folacin': 'Folacin',
    'folate': 'Folate',
    'vitaminb12': 'Vitamin B12',
    'pantothenicacid': 'Pantothenic Acid',
    'pantothenate': 'Pantothenate',
    'alcohol': 'Alcohol',
    'carbohydrate': 'Carbohydrate',
    'erythritol': 'Erythritol',
    'glycerol': 'Glycerol',
    'isomalt': 'Isomalt',
    'lactitol': 'Lactitol',
    'maltitol': 'Maltitol',
    'mannitol': 'Mannitol',
    'polydextrose': 'Polydextrose',
    'sorbitol': 'Sorbitol',
    'xylitol': 'Xylitol',
    'iron': 'Iron',
    'iron_dv': 'Iron',
    'riboflavin': 'Riboflavin',
    'selenium': 'Selenium',
    'magnesium': 'Magnesium',
    'phosphorus': 'Phosphorus',
    'thiamine': 'Thiamine',
    'zinc': 'Zinc'
}

VALID_NUTRIENT_COLUMNS = [
    'calories',
    'sodium',
    'sodium_dv',
    'calcium',
    'calcium_dv',
    'totalfat',
    'totalfat_dv',
    'monounsaturated_fat',
    'polyunsaturated_fat',
    'saturatedfat',
    'saturatedfat_dv',
    'omega3fattyacids',
    'transfat',
    'transfat_dv',
    'potassium',
    'potassium_dv',
    'totalcarbohydrate',
    'totalcarbohydrate_dv',
    'dietaryfiber',
    'dietaryfiber_dv',
    'sugar',
    'protein',
    'cholesterol',
    'vitamina',
    'vitamina_dv',
    'vitaminc',
    'vitaminc_dv',
    'vitamind',
    'vitamine',
    'niacin',
    'vitaminb6',
    'folacin',
    'folate',
    'vitaminb12',
    'pantothenicacid',
    'pantothenate',
    'alcohol',
    'carbohydrate',
    'erythritol',
    'glycerol',
    'isomalt',
    'lactitol',
    'maltitol',
    'mannitol',
    'polydextrose',
    'sorbitol',
    'xylitol',
    'iron',
    'iron_dv',
    'riboflavin',
    'selenium',
    'magnesium',
    'phosphorus',
    'thiamine',
    'zinc'
]

EXPECTED_NUTRIENTS = (
    'Sugars',
    'Calories',
    'Sodium',
    'Calcium',
    'Total Fat',
    'Polyunsaturated Fat',
    'Monounsaturated Fat',
    'Saturated Fat',
    'Omega 3',
    'Trans. Fat',
    'Potassium',
    'Total Carbohydrate',
    'Dietary Fiber',
    'Protein',
    'Cholesterol',
    'Vitamin A',
    'Vitamin C',
    'Vitamin D',
    'Vitamin E',
    'Vitamin B6',
    'Folacin',
    'Vitamin B12',
    'Pantothenic Acid',
    'Pantothenate',
    'Alcohol',
    'Carbohydrate',
    'Erythritol',
    'Glycerol',
    'Isomalt',
    'Lactitol',
    'Maltitol',
    'Mannitol',
    'Polydextrose',
    'Sorbitol',
    'Xylitol',
    'Iron',
    'Riboflavin',
    'Folate',
    'Selenium',
    'Magnesium',
    'Niacin',
    'Phosphorus',
    'Thiamine',
    'Zinc'
)
