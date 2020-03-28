def askUntil(ask, condition):
    inputValue = input(ask)
    while not condition(inputValue):
        inputValue = input(ask)
    return inputValue
