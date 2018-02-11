class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print "{} has {} health remaning.".format(self.name,self.health)     

class Dog(Animal):
    def __init__(self,name, health=150):
        super(Dog, self).__init__(name,health)
    def pet(self):
        self.health += 5
        return self
Doggie = Dog("Fido")
Doggie.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self,name,health=170):
        super(Dragon, self).__init__(name,health)
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        Animal.displayHealth(self)
        print "I am a Dragon!"
dragon = Dragon("Trogdor")
dragon.walk().walk().walk().run().run().fly().displayHealth()