import unittest
from Classes.ingredients import Ingredient
from Classes.recipes import Recipe
from Classes.menu_items import MenuItem

class TestIngredients(unittest.TestCase):
    def test_ingredient_creation(self):
        water = Ingredient("Water", unit="ml", unit_cost=0.0, amount=500)
        self.assertEqual(water.name, "Water")
        self.assertEqual(water.unit, "ml")
        self.assertEqual(water.unit_cost, 0.0)
        self.assertEqual(water.amount, 500)

class TestRecipes(unittest.TestCase):
    def test_recipe_creation(self):
        burger_buns_ingredients = {
            Ingredient("Water"): 170,
            Ingredient("Butter"): 0.1834,
            Ingredient("Egg"): 1,
            Ingredient("Flour"): 0.4720,
            Ingredient("Sugar"): 0.0504,
            Ingredient("Salt"): 0.0063,
            Ingredient("Yeast"): 22
        }
        burger_buns = Recipe("Burger_Buns", burger_buns_ingredients)
        self.assertEqual(burger_buns.name, "Burger_Buns")
        self.assertEqual(burger_buns.ingredients, burger_buns_ingredients)

class TestMenuItems(unittest.TestCase):
    def test_menu_item_creation(self):
        cheese_burger_with_fries = MenuItem(
            "Cheese Burger with Fries",
            {"Onion": 0.0020, "Tomato": 0.0800, "Lettuce": 0.0635, "Ground_Beef": 0.5000, "Black_Pepper": 3.0000, "Cheese_Slice": 1.0000, "French_Fries": 0.2500, "Canola_Oil": 2, "Salt": 0.0030},
            ["Burger_Buns"],  # Pass a list of recipe names
            [0.1250],  # Corresponding amounts
            sell_price=7.77
        )
        self.assertEqual(cheese_burger_with_fries.name, "Cheese Burger with Fries")
        self.assertEqual(cheese_burger_with_fries.ingredients["Onion"], 0.0020)
        self.assertEqual(cheese_burger_with_fries.recipe_names, ["Burger_Buns"])

if __name__ == '__main__':
    unittest.main()