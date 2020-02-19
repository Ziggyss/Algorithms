#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = [0] * len(recipe)
  i = 0
  for key in recipe: 
    if key in ingredients:
      if ingredients[key] < recipe[key]:
        return 0
      else:
        batches[i] = (ingredients[key]//recipe[key])
        i += 1
  return min(batches)

 
      
 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 50, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))