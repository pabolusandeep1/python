class BC:                             ###BOOKING CLASS
    def __init__(self, y, z):                    ###INIT CONSTRUCTOR
        self.economy_class = y
        self.business_class = z

    def get_Economy_class(self):
        print("Class:" + str(self.economy_class))

    def get_business_class(self):
        print("Class:" + str(self.business_class))


class ft:                                    ###flight CLASS
    def __init__(self, i, j):                     ###INIT CONSTRUCTOR
        self.ft_number = i
        self.ft_name = j

    def get_ft_number(self):
        print("ftNumber:" + str(self.ft_number))

    def get_ft_name(Self):
        print("ftName:" + str(self.ft_name))


class Seat:                                         ####SEAT CLASS
    def __init__(self, n, p):                      ###INIT CONSTRUCTOR
        self.seat_number = n
        self.seat_letter = p

    def get_seat_number(self):
        print("SeatNumber:" + str(self.seat_number))

    def get_seat_letter(self):
        print("SeatLetter:" + str(self.seat_letter))


class Person:                                      ####PERSON CLASS
    count = 0

    def __init__(self, a, b, c, d):              ###INIT CONSTRUCTOR
        self.person_first_name = a
        self.person_last_name = b
        self.__person_age = c
        self.person_ticket_ID = d

        Person.count += 1

    def get_person_first_name(self):
        print("PersonFirstName:" + str(self.person_first_name))

    def get_person_last_name(self):
        print("PersonLastName:" + str(self.person_last_name))

    def get_person_age(self):
        print("PersonAge:" + str(self.__person_age))

    def get_person_ticket_ID(self):
        print("PersonTicketID:" + str(self.person_ticket_ID))


p11 = Person("sandy", "p", "23", "246813579")
p22 = Person("marsh", "mallo", "21", "135792468")

#####****p11****###
p11.get_person_first_name()
p11.get_person_age()
p11.get_person_ticket_ID()

#####****p22****###
p22.get_person_first_name()
p22.get_person_age()
p22.get_person_ticket_ID()


####*****MultipleInheritence****#####

#### created one class passenger to inherit person,seat,ft and Booking classes ####
###PASSENGER CLASS
class Passenger(Person, Seat, BC, ft):  ###using 4 primary classes##
    def __init__(self, a, b, c, d, n, p, y, z):            ###INIT CONSTRUCTOR
        Person.__init__(self, a, b, c, d)
        Seat.__init__(self, n, p)
        BC.__init__(self, y, z)  ###super class constructor calling####


### Person3 OBJECT###
p33 = Passenger("kyathy", "bunn","60", "9999999999999", "00", "XX", "economy","business")
p33.get_person_first_name()
p33.get_person_last_name()
#p33.get_person_age()
#p33.get_seat_number()
#p33.get_seat_letter()
p33.get_Economy_class()
