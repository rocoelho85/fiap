from src.inputlib.helpers import askUntil

class ImcCategory:
    def __init__(self, rangeMin, rangeMax, description):
        self.rangeMin = rangeMin
        self.rangeMax = rangeMax
        self.description = description

categories = [
    ImcCategory(0, 15.99, "Baixo peso Grau III"),
    ImcCategory(16, 16.99, "Baixo peso Grau II"),
    ImcCategory(17, 18.49, "Baixo peso Grau I"),
    ImcCategory(18.50, 24.99, "Peso ideal"),
    ImcCategory(25.00, 29.99, "Sobrepeso"),
    ImcCategory(30.00, 34.99, "Obesidade Grau I"),
    ImcCategory(35.00, 39.99, "Obesidade Grau II"),
    ImcCategory(40.00, 1000, "Obesidade Grau III"),
]

def calculateImc(weight, heigth):
    return (weight / (heigth ** 2))

def getCategory(imc):
    for cat in categories:
        if (imc >= cat.rangeMin and imc <= cat.rangeMax):
            return cat.description
    return ""

def validInput(inputValue):
    try:
        castValue = float(inputValue)
        if (castValue > 0):
            return True
    except:
        return False

def run():
    weight = askUntil('Informe seu peso -> ', validInput)
    heigth = askUntil('Informe sua altura -> ', validInput)
    return getCategory(calculateImc(float(weight), float(heigth)))
