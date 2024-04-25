# Menu_Planner
This repository is the beginning of a food service project I am working on tentatively called Restaurant_One. Menu_Planner is just the first portion of this project. The whole scope of this project will be Restaurant Management tools, seperate apps that connect information from Reservations, to Equiptment Monitoring, to Inventory Control etc... everything will connect to provide complete control of a restaurant or food service business. I would also like to implement AI assistance into this program at all levels.

My goal in Menu_Planner is to have a working program that allows you to build recipes and menu items based on a database of ingredients. This program will have capabilites to add ingredients manually or from a database or document from food service suppliers. It's primary function is to build and cost out menus.

I am still learning Python and will be happy to accept critiques.
In this Python code I have created 3 classes

1:
           Ingredients
              
    A Ingredient should be an object that that will make up Recipes and MenuItems.
    The functions of Ingredients are to state the cost of the Ingredient in relation to it's unit. 
    A Ingredient is also a dictionary. Ingredients will be called for many parts of this project, like in recipes, menu items, ordering, inventory, waste managment, usage, cost control, etc...
    There will be sub classes like Produce_Ingredients, and Meat_Ingredients. These sub classes increase functionality by allowing us to know what category of ingredient this falls under. Ingredients will also be sorted by suppliers (**make suppliers section yet?**). Some suppliers might offer the same Ingredients as another supplier. Invoices will be used to update the current cost of Ingredients.(**make invoices section yet?**). 
    AI could be built into this project, using the ingredient class to help source ingredients based on many different factors. ie. quality, local, seasonal, cost, authenticity etc...

2:
            Recipes
              
    A Recipe is an object that that is comprised of ingredients and sub_recipes.
    The functions of Recipe are to calculate the cost of the Recipe, show a recipe card that includes directions and a Recipe is also a dictionary. Recipes get called into menuitems, inventory, alergy guides, recipe book, portion control, waste management, KDS/kitchen comunications, bar recipes, bar comunications, etc...
    AI could be built into this project, using the recipe class to help build recipes, offer suggestions on ingredients that go well in the recipe. offer suggestions on quantities of each ingredient. AI should be able to generate a Method/Directions on a list of ingredients you provided.


3:
            Menu Items
              
    A MenuItem should be an object that that is comprised of ingredients and recipes.
    The functions of MenuItem are to calculate the cost of the Item, to determine the sell_price and create MenuItem dictionary to later build a current menu. A Menu Item can be called to cost a menu, to build a new menu, for KDS/kitchen communications, tracking sales/inventory, to creat spec sheets, portion control, alergy guides, waste management, etc...        
