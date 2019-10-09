#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  pass
  # Check if all ingredients from the recipe are available, if not, return 0
  # for key, value in recipe.items()
  ing_keys = ingredients.keys()
  recipe_keys = recipe.keys()

  for item in (ing_keys and recipe_keys):
    print(str(item))



  # Check how many times each ingredient is present in quantity

  # If > 0, check what is the smallest number and return it
  return True


rec = { 'milk': 100, 'butter': 50, 'flour': 5 }
ing = { 'milk': 132, 'butter': 48, 'flour': 51 }

test = recipe_batches(rec,ing)
print(test)

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))