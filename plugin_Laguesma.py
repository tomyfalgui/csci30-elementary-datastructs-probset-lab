#error at 5th case
word = list(input())
output = list()
size = len(word)-1
count = 0
status = False
while count < size:
    size = len(word)-1
    count2 = count+1
    size1 = len(word)-1
    while count2 < size1+1:
        if (word[count] == word[count2]):
            status = True
            word.pop(count)
            word.pop(count2-1)
            count = 0
            count2=0
            break
        else:
            status = False
            count2+=1
    if status == False:
        count += 1
    status=False

print (*word, sep='')

