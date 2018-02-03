#importing the regular expressions in python
import re
k = input('Enter a sentence: \n')  # taking input from the user
temp = re.sub("[^\w]", " ",  k).split()# splitting up the given input into elements
s=len(temp) #calculating the length of the input
def middlechar(input_list):  #fuction for calculating the middle word
    l=len(input_list)
    middle = float(len(input_list))/2
    if l % 2 == 0:
        return (input_list[int(middle)], input_list[int(middle-1)])
    else:
        return input_list[int(middle - .5)]

y = middlechar(temp)# calling the function middlechar
print('\n The middle word/words is: ', y)

srtlist=sorted(temp,key=len)
print('\nThe longest charecter is: ',srtlist[-1])

revwords=' '.join(w[::-1] for w in k.split())
print('\nReverse of the sentence is: ',revwords)