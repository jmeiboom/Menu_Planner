from Classes.ingredients import Ingredient, ingredients_dict
from Classes.recipes import Recipe, recipes_dict

"""      
             Menu Items
              v.0.001
              
    A MenuItem should be an object that that is comprised of ingredients and recipes.
    The functions of MenuItem are to calculate the cost of the Item, and to determine the sell_price. A MenuItem is also a dictionary
    
"""

class MenuItem:
    def __init__(self, name, ingredients, recipe_names, recipe_amounts, food_cost_percentage=None, sell_price=None):
        if not isinstance(ingredients, dict):
            raise TypeError("Ingredients must be provided as a dictionary.")

        for ingredient, amount in ingredients.items():
            if not isinstance(amount, (int, float)) or amount < 0:
                raise ValueError(f"Invalid amount for ingredient {ingredient.name}. Amount must be a non-negative number.")

        if not isinstance(recipe_names, list):
            raise TypeError("Recipes must be provided as a list.")

        if not isinstance(recipe_amounts, list):
            raise TypeError("Recipe amounts must be provided as a list.")

        if len(recipe_names) != len(recipe_amounts):
            raise ValueError("The number of recipes must match the number of recipe amounts.")

        self.name = name
        self.ingredients = ingredients
        self.recipes = [recipes_dict[recipe_name] for recipe_name in recipe_names]  # Access each recipe separately
        self.recipe_amounts = recipe_amounts
        
        if food_cost_percentage is not None:
            if not 0 <= food_cost_percentage <= 1: 
                raise ValueError("Food cost percentage must be a value between 0 and 1.")
            
        self.food_cost_percentage = food_cost_percentage
        self.sell_price = sell_price

    def calculate_cost(self):
        total_cost = 0

        for ingredient_name, quantity in self.ingredients.items():
            ingredient = ingredients_dict.get(ingredient_name)
            if ingredient is None:
                raise ValueError(f"Ingredient {ingredient_name} is not found in the ingredients dictionary.")
            if not isinstance(quantity, (int, float)) or quantity < 0:
                raise ValueError(f"Invalid quantity for ingredient {ingredient_name}. Quantity must be a non-negative number.")
            if "unit_cost" not in ingredient:
                raise AttributeError(f"Ingredient {ingredient_name} does not have a unit_cost attribute.")
            total_cost += ingredient["unit_cost"] * quantity
    
        for recipe, amount in zip(self.recipes, self.recipe_amounts):
            if not isinstance(amount, (int, float)) or amount < 0:
                raise ValueError("Invalid recipe amount. Recipe amount must be a non-negative number.")
            scaled_recipe_cost = recipe.recipe_cost * amount
            total_cost += scaled_recipe_cost

        if self.food_cost_percentage is not None:
            if not isinstance(self.food_cost_percentage, (int, float)) or self.food_cost_percentage <= 0:
                raise ValueError("Invalid food cost percentage. Food cost percentage must be a positive number.")
            self.sell_price = total_cost / self.food_cost_percentage
        elif self.sell_price is not None:
            if not isinstance(self.sell_price, (int, float)) or self.sell_price <= 0:
                raise ValueError("Invalid sell price. Sell price must be a positive number.")
            self.food_cost_percentage = total_cost / self.sell_price

        return total_cost

cheese_burger_with_fries = MenuItem(
    "Cheese Burger with Fries",
    {"Onion": 0.0020, "Tomato": 0.0800, "Lettuce": 0.0635, "Ground_Beef": 0.5000, "Black_Pepper": 3.0000, "Cheese_Slice": 1.0000, "French_Fries": 0.2500, "Canola_Oil": 2, "Salt": 0.0030},
    ["Burger_Buns", "Mayonnaise"],  # Pass a list of recipe names
    [0.1250, 0.0634],  # Corresponding amounts
    sell_price=7.77
)

cheese_burger_with_fries.calculate_cost()
cheese_burger_with_fries_cost = cheese_burger_with_fries.calculate_cost()

menu_item_dict = {
    "Cheese Burger with Fries": cheese_burger_with_fries,
    # Add more recipes as needed...
}