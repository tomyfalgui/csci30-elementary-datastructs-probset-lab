from collections import deque
s = ""
output = []

try:
	while True:
		a = input()
		if a == '':
			break
		else:
			s = a
			val = deque([])
			pointer = 0
			for letter in s:
				if letter == '[':
					pointer = 0
				elif letter == ']':
					pointer = len(val)
				else:
					val.insert(pointer, letter)
					pointer+= 1

			output.append(''.join(val))
except EOFError:
	pass

		

for o in output:
	print(o)

# 24157937 tomy8910