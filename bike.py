class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print "Price: {}".format(self.price)
        print "Max Speed: {}".format(self.max_speed)
        print "Miles Driven: {}".format(self.miles)
        return self
    def ride(self):
        print "Riding..."
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing..."
        self.miles -= 5
        return self

first = Bike("150","20")
second = Bike("200", "30")
third  = Bike("500", "40")

first.ride().ride().ride().reverse().displayinfo()
second.ride().ride().reverse().reverse().displayinfo()
third.reverse().reverse().reverse().displayinfo()