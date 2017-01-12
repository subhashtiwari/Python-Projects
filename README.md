# Python-Projects
This contains various projects on Python which i made when i was learning it.

# In this code we have used Inheritance and Method Overriding 

class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color
            
    def show_info(self):
        print("Last Name : "+self.last_name)
        print("Eye Color : "+self.eye_color)
        
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name : "+self.last_name)
        print("Eye Color : "+self.eye_color)
        print("Number of Toys : "+str(self.number_of_toys))

james_potter = Parent("Potter", "Blue")
#james_potter.show_info()

harry_potter = Child("Potter", "Blue", 1)
harry_potter.show_info()

#print(james_potter.last_name)
#print(harry_potter.last_name)
#print(harry_potter.number_of_toys)

