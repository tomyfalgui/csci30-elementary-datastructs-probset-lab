#time limit exceeded
word = list(input())
stack = []
wordSize = len(word)-1
counter = 0
while counter <= wordSize:

    wordSize = len(word) - 1
    if wordSize >0:

        if wordSize > 0 and word[counter] == '[':
            count = 0
            while word[counter] != ']' and len(word) > 0:
                stack.insert(count,word.pop(0))
                count += 1

                wordSize = len(word) - 1
                if wordSize==-1 :
                    break

        if wordSize > 0 and word[counter] == ']':
            while word[counter] != '[' and len(word) > 0:
                stack.append(word.pop(0))
                wordSize = len(word) - 1
                if wordSize == -1:
                    break

        if wordSize>0:
            stack.append(word.pop(0))
        if wordSize ==0:
            break
counter = 0
stackSize = len(stack)-1
finalSize =[]
while counter <= stackSize:
    if stack[counter] != ']' and stack[counter] != '[':
        finalSize.append(stack[counter])
    counter += 1


print (*finalSize, sep ='')
