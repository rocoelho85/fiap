from ..inputlib.helpers import askUntil
from ..validationlib.validation import validFoodQty, validCalories

def exec():
  foodCalories = []
  foodQty = int(askUntil('Informe a quantidade de refeições -> ', validFoodQty))
  currentFood = 1
  while currentFood <= foodQty:
    calories = float(askUntil('Informe a quantidade de calorias da refeição ' + str(currentFood) + ' -> ', validCalories))
    foodCalories.append(calories)
    currentFood = currentFood + 1
  print(foodCalories)
