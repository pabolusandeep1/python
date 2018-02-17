#Code to print the books in the given range by the user
dict={"a" : "20", "b" : "25", "c" : "30", "d" : "35", "e" : "40"} #setting up the lib
print("The current books are present in the library: \n", dict)
x=int(input("Enter the starting price range of the books : "))
y=int(input("Enter the final pricing range of the books : "))
print("Books falling in the range within the dictionary :\n")
for name,num in dict.items():
    if int(num) in range(x,y+1):
        print('%s' %(name))