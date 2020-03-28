def greaterThanZero(value):
  if (value > 0):
    return True 
  else:
    return False

def validFoodQty(value):
  try:
    castValue = int(value)
    return greaterThanZero(castValue)
  except:
    return False

def validCalories(value):
  try:
    castValue = float(value)    
    return greaterThanZero(castValue)
  except:
    return False
