class SignatureType:
    def __init__(self, levelName, percentage):
        self.levelName = levelName
        self.percentage = percentage


signature_types = [
    SignatureType("Basic", 30),
    SignatureType("Silver", 20),
    SignatureType("Gold", 10),
    SignatureType("Platinum", 5)
]


def validInput(inputValue):
    try:
        castValue = float(inputValue)
        if (castValue > 0):
            return True
    except:
        return False


def validLevel(level):
    return level in list(map(lambda sig: sig.levelName, signature_types))


def getSignaturePercentage(level):
    for sig in signature_types:
        if (sig.levelName == level):
            return sig.percentage
    return ""


def calculateBonus(revenue, percentage):
    return revenue * (percentage / 100)


client_level = ""
while not validLevel(client_level):
    client_level = input("Informe o nível de assinatura do cliente -> ")

revenue = 0
while not validInput(revenue):
    revenue = input("Informe o faturamento anual do client -> ")

print(calculateBonus(float(revenue), getSignaturePercentage(client_level)))
