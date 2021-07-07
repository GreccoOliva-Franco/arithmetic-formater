def arithmetic_arranger(problems,*args):
	# Auxiliar functions:
	def solve(top, op, bottom):
		if op == "+":
			res = int(top) + int(bottom)
		else:
			res = int(top) - int(bottom)

		return res

	def checkOperands(top, bot):
		isValid = False

		if top.isnumeric() and bot.isnumeric():
			isValid = True
		
		return isValid

	def checkNumLength(top, bot):
		isValid = True

		if len(top) > 4 or len(bot) > 4:
			isValid = False

		return isValid

	def checkOperation(operation):
		isValid = False

		if operation == "+" or operation == "-":
			isValid = True

		return isValid

	def checkNumberOperations(operationList):
		isValid = False

		if len(operationList) <= 5:
			isValid = True

		return isValid

	# Settings:
	fourSpaces = " " * 4		
	topList = []
	bottomList = []
	lineList = []
	resultsList = []

	# Problem parser:
	if not checkNumberOperations(problems):
		return "Error: Too many problems."

	for problem in problems:
		topNumber = problem.split(" ")[0]
		operation = problem.split(" ")[1]
		bottomNumber = problem.split(" ")[2]

		if not checkOperation(operation):
			return "Error: Operator must be '+' or '-'."

		if not checkOperands(topNumber, bottomNumber):
			return "Error: Numbers must only contain digits."

		if not checkNumLength(topNumber, bottomNumber):
			return "Error: Numbers cannot be more than four digits."

		result = solve(topNumber, operation, bottomNumber) 
		topLength = len(topNumber)
		bottomLength = len(bottomNumber)

		stringLength = max([topLength, bottomLength]) +2

		topString = topNumber.rjust(stringLength)
		bottomString = operation + " " + bottomNumber.rjust(stringLength - 2)
		lineString = "-" * stringLength
		resultString = str(result)
		topList.append(topString)
		bottomList.append(bottomString)
		lineList.append(lineString)
		resultsList.append(resultString.rjust(stringLength))

	
	responseList = [fourSpaces.join(topList), fourSpaces.join(bottomList), fourSpaces.join(lineList)]
	if len(args) > 0:
		if args[0] == True:
			responseList.append(fourSpaces.join(resultsList))

	response = "\n".join(responseList) 
	# print(response)

	# print("***********************************************************************************")
	return response
