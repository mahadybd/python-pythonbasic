#Inheritance---------------
from collections import UserString


class User:
    def log(self):
        print(self)
#End Inheritance-----------

#Polymorphism----------
class Teacher(User):
    def log(self):
        print("I am a teacher")

class Customer(User):
    def log(self):
        print("I am a customer")

    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        # print("customer created")

    #Encapsulation-------------------------
    @property
    def  name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self):
        del self._name
    #End Encapsulation---------------------

    def update_membership(self, new_membership):
        self.membership_type = new_membership

    #static method. Only invoed with class name it self, not with any object(like: customers[1]. read_customer())
    def read_customer():
        print("Reading customer from DB")

    def __str__(self):
        print("Converting to string")
        return self.name + " " + self.membership_type

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    #over writing method
    # __hash__ = None

    #over writing method
    __repr__ = __str__
    
    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False

# c = Customer("Mahady", "Gold")
# print(c.name, c.membership_type)

# c2 = Customer("Hasan", "Bronze")
# print(c2.name, c2.membership_type)

customers = [Customer("Mahady", "Gold"), Customer("Mahady", "Bronze"), Teacher()]

# print(customers[1].membership_type)
customers[1].update_membership("Gold")
# print(customers[1].membership_type)

# Customer.read_customer()

#print readable value only possible for __str__ method (convert to string)
# print(customers[1])

#print all customers
# Customer.print_all_customers(customers)

#invoked __eq__ method
# print(customers[0] == customers[1])

# only possible for  __repr__ method 
# del customers[0].name
# print(customers)

#Polymorphism----------
# customers[2].log()

users = [Customer("Mahady", "Gold"), Customer("Mahady", "Bronze"), Teacher()]

for user in users:
    user.log()



