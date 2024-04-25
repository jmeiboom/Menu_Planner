
"""      
            Ingredients
              v.0.001
              
    A Ingredient should be an object that that will make up Recipes and MenuItems.
    The functions of MenuItem are to state the cost of the Ingredient in relation to it's unit. A Ingredient is also a dictionary
    
"""

class Ingredient:
    def __init__(self, name, unit="", unit_cost=0.0, amount=1.0):

        def __str__(self):
            return f"Name: {self.name}, Unit: {self.unit}, Unit Cost: {self.unit_cost}, Amount: {self.amount}"
       
        # Check if unit_cost is a non-negative number
        if not isinstance(unit_cost, (int, float)) or unit_cost < 0:
            raise ValueError("Unit cost must be a non-negative number.")
        
        # Check if amount is a non-negative number
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Amount must be a non-negative number.")
        
        self.name = name
        if unit == "" and unit_cost == 0.0:
                    # Look up unit and unit_cost from ingredients_dict
                    if name in ingredients_dict:
                        self.unit = ingredients_dict[name]["unit"]
                        self.unit_cost = ingredients_dict[name]["unit_cost"]
                    else:
                        raise ValueError(f"No data found for ingredient {name} in ingredients_dict.")
        else:
            self.unit = unit
            self.unit_cost = unit_cost
            self.amount = amount


# Define the dictionary of ingredients
ingredients_dict = {
    "Water": {"unit": "ml", "unit_cost": 0.0000},
    "Butter": {"unit": "lb", "unit_cost": 3.7000},
    "Egg": {"unit": "ea", "unit_cost": .3300},
    "Flour": {"unit": "kg", "unit_cost": 1.2500},
    "Sugar": {"unit": "kg", "unit_cost": 1.9000},
    "Salt": {"unit": "kg", "unit_cost": 0.5600},
    "Yeast": {"unit": "g", "unit_cost": 0.0099},
    "Dijon_Mustard": {"unit": "ml", "unit_cost": 0.0114},
    "Olive_Oil": {"unit": "ml", "unit_cost": 0.0149},
    "White_Wine_Vinegar": {"unit": "ea", "unit_cost": 0.0027},
    "Lemon": {"unit": "ea", "unit_cost": 0.5700},
    "White_Pepper": {"unit": "g", "unit_cost": 0.0166},
    "Onion": {"unit": "kg", "unit_cost": 2.3344},
    "Tomato": {"unit": "ea", "unit_cost": 0.3643},
    "Lettuce": {"unit": "head", "unit_cost": 2.4996},
    "Ground_Beef": {"unit": "lbs", "unit_cost": 0.9490},
    "Black_Pepper": {"unit": "g", "unit_cost": 0.0316},
    "Cheese_Slice": {"unit": "ea", "unit_cost": 0.3435},
    "French_Fries": {"unit": "kg", "unit_cost": 3.1564},
    "Canola_Oil": {"unit": "ml", "unit_cost": 0.0034},
    "Garlic": {"unit" : "clove", "unit_cost": 0.0145}
    # Add more ingredients as needed
}
