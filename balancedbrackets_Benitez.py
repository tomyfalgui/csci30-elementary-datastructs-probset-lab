balancedCheck = False
notifier = False

amountRun = int(input())
answerArray = []

def compareBrackets():
	stackElement = stackBracket.pop()
	queueElement = queueBracket.pop(0)
	if(stackElement is '{'):
		if(queueElement is '}'):
			return True
		else:
			return False
	elif(stackElement is '('):
		if(queueElement is ')'):
			return True
		else:
			notifier = True
			return notifier
	elif(stackElement is '['):
		if(queueElement is ']'):
			return True
		else:
			return False
	else:
		return False

for a in range(int(amountRun)):
	startingBrackets = list(input()) 
	lenBracket = len(startingBrackets)
	stackBracket = []
	queueBracket = []
	for b in range(int(lenBracket)):
		if(startingBrackets[b] is '(' or startingBrackets[b] is '{' or startingBrackets[b] is '['):
			stackBracket.append(startingBrackets[b])
		elif(startingBrackets[b] is ')' or startingBrackets[b] is '}' or startingBrackets[b] is ']'):
			queueBracket.append(startingBrackets[b])
	if(len(stackBracket) == len(queueBracket)):
		balancedCheck = True
	else:
		balancedCheck = False
		answerArray.append('NO')

	if(balancedCheck):
		stackBracket = []
		queueBracket = []
		for c in range(lenBracket):
			if(startingBrackets[c] is '{' or startingBrackets[c] is '(' or startingBrackets[c] is '['):
				stackBracket.append(startingBrackets[c])
			elif(startingBrackets[c] is ')' or startingBrackets[c] is '}' or startingBrackets[c] is ']'):
				if(len(stackBracket) == 0):
					notifier = False
					break
				queueBracket.append(startingBrackets[c])
				notifier = compareBrackets()
				if(notifier == False):
					break
		if(notifier == False):
			answerArray.append('NO')
		elif(notifier == True):
			answerArray.append('YES')


for d in range(int(len(answerArray))):
	print(answerArray[d])