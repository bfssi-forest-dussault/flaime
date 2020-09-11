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
    "Not Food"
]

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
