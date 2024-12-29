# multiple inheritance = inherit from more than one parent class
#  C( A, B)
# multiple level inheritance = inherit from a parent which inherited from another parent
# C(B)<- B(A)<-A

class Aninmal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is sleeping!")


class Prey(Aninmal):
    def flee(self):
        print(f"{self.name} is fleeing!")


class Predator(Aninmal):
    def hunt(self):
        print(f"{self.name} is hunting!")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Predator, Prey):
    pass


rabbit = Rabbit("BUG")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.eat()
rabbit.sleep()
# rabbit.hunt()  - do not have this attribute 
rabbit.flee()
print()
hawk.eat()
hawk.sleep()
hawk.hunt()
# hawk.flee()  - do not have this attribute
print()
fish.eat()
fish.sleep()
fish.hunt()
fish.flee()
