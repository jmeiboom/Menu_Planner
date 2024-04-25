from Classes.recipes import Recipe, recipes_dict
from Classes.ingredients import ingredients_dict

# def build_recipe(name, ingredients, amounts, units):
#     """
#     Build a recipe with the given name, ingredients, amounts, and units.
    
#     Args:
#         name (str): the name of the recipe.
#         ingredients (list): A list of Ingredient Objects.
#         amounts (list): A list of amounts correspinding to each ingredient.
        
#     Returns:
#         Recipe: The constructed Recipe object.
#     """

#     if len(ingredients) != len(amounts) or len(amounts) != len(units):
#         raise ValueError("Lengths of ingredients, amounts, and units must match.")
    
#     ingredient_dict = {}
#     for ingredient, amount, unit in zip(ingredients, amounts, units):
#         ingredient_dict[ingredient] = {"amount": amount, "unit": unit}

#         return Recipe(name, ingredients_dict)



def create_recipe_from_user_input():
    # Get user input for recipe name
    recipe_name = input("Enter the name of the recipe: ")

    # Initialize empty dictionaries for ingredients and sub recipes
    ingredients = {}
    sub_recipes = {}

    # Get user input for ingredients
    while True:
        ingredient_name = input("Enter the name of an ingredient or type 'done' to finish): ")
        if ingredient_name.lower() == 'done':
            break
        ingredient_amount = float(input(f"Enter the amount of {ingredient_name}: "))
        ingredient_unit = input(f"Enter the unit of measurement for {ingredient_name}: ")
        ingredients[ingredient_name] = {"amount": ingredient_amount, "unit": ingredient_unit}

    # Get user input for sub recipes
    while True:
        sub_recipe_name = input("Enter the name of a sub-recipe (or type 'done' to finish): ")
        if sub_recipe_name.lower() == 'done':
            break
        sub_recipe_amount = float(input(f"Enter the amount of {sub_recipe_name}: "))
        sub_recipes[sub_recipe_name] = sub_recipe_amount

    # Get user input for recipe directions
    directions = input("Enter the directions for the recipe (press Enter if not available): ")

    # Create the Recipe object
    recipe = Recipe(name=recipe_name, ingredients=ingredients, sub_recipes=sub_recipes, directions=directions)

    return recipe

# Example usage:
user_recipe = create_recipe_from_user_input()