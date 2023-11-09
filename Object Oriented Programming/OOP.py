'''
OBJECT ORIENTED PROGRAMMING
Object oriented programming is a programming model that organises software design around data or objects
rather than functions and logic.
An object can be defined as a data field with unique attributes and behaviour.
OOP focuses on objects developers want to manipulate.

ADVANTAGES/USES
OOP is well suited for programs that are large, complex and actively updated or maintained.
Used for projects of manufacturing and design.
Used for moble applications.
Can be used for manufacturing system simulation software.
It is beneficial for collaborative development where the project is divided into groups.
Enables code reusability , scalability and effeciency.

CLASSES
Classes are user-defined data types that act as the blueprint for individual objects, attributes and methods.

OBJECTS
Objects are instances of a class created with specifically defined data.
Objects correspond to real-world objects or an abstract entity.
'''
#User class with properties name, age, location
class Users:
    name= "Jolline"
    age= 20
    location= "Kireka"
user1= Users()
print(user1.name)
print(user1.age)
    
    

class User:
    def __init__(self, name, age, location):
        self.name= name
        self.age= age
        self.location= location
User1= User("Mbabazi Hawa",19, "Bukoto")

print(User1.name)
print(User1.age)
print(User1.location)