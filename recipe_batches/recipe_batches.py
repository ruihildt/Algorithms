#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # Loop through recipe for all ingredients and quantity
  max_batches = []
  for ingredient, quantity in recipe.items():
    # Check if all ingredients from the recipe are available, if not, return 0
    if ingredient in ingredients:
      # Check how many full batch we can make with each ingredient
      batches = int(ingredients[ingredient] / recipe[ingredient])
      # If there's a mininmum of 1 batch, add it to the max list, if not, return 0
      if 1 <= batches:
        max_batches.append(batches)
    else:
      return 0

  # Return max number of batch
  max_batch = min(max_batches)

  return max_batch

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))