from src.inputlib.helpers import askUntil
from src.validationlib.validation import greaterOrEqualThenZero, validInt


class VoteWeekday:
    def __init__(self, weekday, qtyVote):
        self.weekday = weekday
        self.qtyVote = int(qtyVote)


def validVote(inputValue):
    return validInt(inputValue) and greaterOrEqualThenZero(inputValue)


weekdays = [
    "Segunda-Feira",
    "Terça-Feira",
    "Quarta-Feira",
    "Quinta-Feira",
    "Sexta-Feira"
]


def run():
    lastHighestVote = 0
    biggerVoteWeekday = {}
    for weekday in weekdays:
        qtyVote = askUntil('Informe o total de votos para ' +
                           weekday + ' -> ', validVote)
        if (int(qtyVote) > lastHighestVote):
            biggerVoteWeekday = VoteWeekday(weekday, qtyVote)
            lastHighestVote = int(qtyVote)

    print("O dia com mais votos é " + biggerVoteWeekday.weekday +
          " com " + str(biggerVoteWeekday.qtyVote) + " votos")
