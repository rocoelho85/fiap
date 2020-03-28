class VoteWeekday:
	def __init__(self, weekday, qtyVote):
		self.weekday = weekday
		self.qtyVote = int(qtyVote)

def validInput(inputValue):
	try:
		castValue = int(inputValue)
		if (castValue > 0):
			return True
	except:
		return False

weekdays = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira"]
lastHighestVote = 0
voteWeekday = {}
for weekday in weekdays:
	qtyVote = 0
	while not validInput(qtyVote):
		qtyVote = input("Informe o total de votos para " + weekday + " -> ")
	if (int(qtyVote) > lastHighestVote):
		voteWeekday = VoteWeekday(weekday, qtyVote)
		lastHighestVote = int(qtyVote)


print("O dia com mais votos é " + voteWeekday.weekday + " com " + str(voteWeekday.qtyVote) + " votos")