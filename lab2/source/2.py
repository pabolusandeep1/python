import switch as switch

contact_list = [{"name" : 'joe', "number":123456, "email":"joe@gmail.com"},
                {"name" : "jim", "number":1234567, "email":"jim@gmail.com"},
                {"name" : "mikel","number":13456789,"email":"mikel@gmail.com"},
                {"name" : "jackie", "number":98765432, "email": "jackie@gmail.com"}]


while True:
    print('''This is the address book .what do you want to do!  
            1.) display contact by name        2.) display contact by number
            3.) Edit a contact by name         4.) Quit''')

    choice = input("Select an option: ")
    if choice == "1":
        nm = input("Enter name to get contact: ")
        for i in contact_list:
            if nm in i.values():
                print(i)

    elif choice == "2":
      num = int(input("enter contact: "))
      for j in contact_list:
           if num in j.values():
               print(j)

    elif choice == "3":
       nme = input("enter name to edit:")
       for k in contact_list:
           if nme in k.values():
               print(k)
               newnum = int(input("enter number to edit"))
               k["number"] = newnum
               print(k)
    elif choice == "4":
       print("Program quit!")
       break
    else:
        print("No relative input.Check again")
    break