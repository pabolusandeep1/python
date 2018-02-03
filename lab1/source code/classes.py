#to find the common word in 2 lists and to print non-common words in the list
def com_name(list1, list2):#function for finding the common elements
    result = []
    for element in list1:#loop for finding the common elements
        if element in list2:
            result.append(element)
    return result


def noncom(full, x):#function for finding the non-common elements
    result = []
    for element in full:#loop for finding the non common elements
        if element not in x:
            result.append(element)
    return result



li1 = input("Enter the students in Python class: ")#input for the 1st list from customer
list1 = li1.split()#splitting up the words
li2 = input("Enter the students in Web Application class: ")#input for the 2nd list from customer
list2 = li2.split()#splitting up the words
print('\nThe students common to both the classes are: ')
x = com_name(list1,list2)
print(x)#calling the function
full = list1 + list2
print ('\nStudents not common in both classes:',noncom(full,x))
