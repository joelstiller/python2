class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.mileage = mileage
        self.fuel = fuel
        if price > 10000:
            self.tax = .015
        else:
            self.tax = .012
        self.displayall()
    def displayall(self):
        print "Price: {}".format(self.price)
        print "Speed: {}".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Mileage: {}".format(self.mileage)
        print "Tax: {}".format(self.tax)
        print ""
        return self

car1 = Car("12000", "Fast", "Lots", "1")
car2 = Car(87423, 5, 'Not Full', 105)
car3 = Car(2000, 15, 'Kind of Full', 95)
car4 = Car(9020, 25, 'Full', 25)
car5 = Car(29800, 45, 'Empty', 25)
car6 = Car(60000, 35, 'Empty', 15)