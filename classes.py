
#Create class

class User:

    #Constructor
    def __init__(self, name, email, age):
        self.name =  name
        self.email = email
        self.age = age
    
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'  

    def has_birthday(self):
        self.age += 1


# Extend class
class Customer(User):
     # Constructor
    def __init__(self, name, email, age):
        User.__init__(self, name, email, age) #Called proper parent class constructor to make this as proper child inehriting all methods.
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    
    def set_balance(self, balance):
        self.balance = balance
    
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and   my balance is {self.balance}'  

#  Init user object
mahady =  User('Mahady Hasan', 'mahady@gmail.com', 35)

# Init customer object
anha = Customer('Anha Mahreen', 'anha@gmail.com', 4)
anha.set_balance(500)


# mahady.has_birthday()
print(anha.greeting())