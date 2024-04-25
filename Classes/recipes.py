from Classes.ingredients import Ingredient

"""      
              Recipes
              v.0.001
              
    A Recipe should be an object that that is comprised of ingredients and sub_recipes.
    The functions of Recipe are to calculate the cost of the Recipe, A Recipe is also a dictionary
    
"""

class Recipe:
    def __init__(self, name, ingredients, sub_recipes=None, directions=None):
        if not isinstance(ingredients, dict):
            raise TypeError("Ingredients must be provided as a dictionary.")
        
        for ingredient, amount in ingredients.items():
            if not isinstance(amount, (int, float)) or amount < 0:
                raise ValueError(f"Invalid amount for ingredient {ingredient.name}. Amount must be a non-negative number.")
        
        self.name = name
        self.ingredients = ingredients
        self.sub_recipes = sub_recipes if sub_recipes is not None else {}
        self.directions = directions
        self.recipe_cost = self.calculate_recipe_cost()

    def calculate_recipe_cost(self):
        total_cost = 0
        for ingredient, amount in self.ingredients.items():
            total_cost += ingredient.unit_cost * amount
        return total_cost

    def get_recipe_steps(self):
        return self.directions if self.directions else "Directions not specified for this recipe."

    def load_recipe_steps_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.directions = file.read()
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("An error occurred:", e)
            
# Example recipes
# Burger Bun Recipe
burger_buns_ingredients = {
    Ingredient("Water"): 170,
    Ingredient("Butter"): 0.1834,
    Ingredient("Egg"): 1,
    Ingredient("Flour"): 0.4720,
    Ingredient("Sugar"): 0.0504,
    Ingredient("Salt"): 0.0063,
    Ingredient("Yeast"): 22
}

burger_buns_directions = ""
burger_buns = Recipe("Burger_Buns", burger_buns_ingredients, directions=burger_buns_directions)
burger_buns.load_recipe_steps_from_file("burger_buns_directions.txt")

# Mayonnaise Recipe
mayo_ingredients = {
    Ingredient("Egg"): 1,
    Ingredient("Dijon_Mustard"): 5,
    Ingredient("Salt"): 0.0003,
    Ingredient("Olive_Oil"): 177.4412,
    Ingredient("White_Wine_Vinegar"): 8,
    Ingredient("Lemon"): 0.5000,
    Ingredient("White_Pepper"): 2
}

mayo_directions = """
Whisk 1 large egg yolk, at room temperature 30 minutes, ½ tsp. Dijon mustard, and ¼ tsp. kosher salt in a small bowl until combined well. Add about ¼ cup olive or vegetable oil (or a combination) drop by drop, whisking constantly until mixture begins to thicken. Whisk in 1 tsp. white-wine vinegar or cider vinegar and 1½ tsp. fresh lemon juice, then add remaining ½ cup oil in a very slow, thin stream, whisking constantly until well blended. If at any time it appears that oil is not being incorporated, stop adding oil and whisk mixture vigorously until smooth, then continue adding oil. Whisk in salt to taste and ¼ tsp. white pepper (if using). Chill, surface covered with plastic wrap, until ready to use.
"""

mayo = Recipe("Mayonnaise", mayo_ingredients, directions=mayo_directions)

# Define a dictionary to store all recipes
recipes_dict = {
    "Burger_Buns": burger_buns,
    "Mayonnaise": mayo,
    # Add more recipes as needed...
}

