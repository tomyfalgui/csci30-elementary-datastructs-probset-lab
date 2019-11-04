typed = input()
no_repeat = []

for letter in typed:
	if len(no_repeat) == 0:
		no_repeat.append(letter)
	elif letter == no_repeat[-1]:
		no_repeat.pop()
	else:
		no_repeat.append(letter)

print(*no_repeat, sep="")