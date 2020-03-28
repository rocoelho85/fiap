def greaterThenZero(value):
    return True if value > 0 else False

def greaterOrEqualThenZero(value):
	return True if value >= 0 else False

def validInt(value):
    return True if type(value) is int else False

def validFloat(value):
    return True if (type(value) is float or type(value) is int) else False
