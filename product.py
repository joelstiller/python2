class Product(object):
    def __init__(self, price, name, weight, brand, status=None):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        if status:
            self.status = status
        else:
            self.status = "For sale"
    def sell(self):
        self.status = 'Sold'
        return self
    def addtax(self, tax):
        print "Total: {}".format(self.price * (tax + 1))
        return self
    def takeback(self,reason):
        if reason == "Defective":
            self.price = 0
            self.status = reason
        elif reason == "Like New":
            self.status = "For Sale"
        elif reason == 'Used':
            self.price *= .8
            self.status = reason
        return self
    def displayinfo(self):
        print "Price: {}".format(self.price)
        print "Name: {}".format(self.name)
        print "Weight: {}".format(self.weight)
        print "Brand: {}".format(self.brand)
        print "Status: {}".format(self.status)
        return self

product1 = Product(20, "Chocolates", 1, "Fancy", "Used")
product1.displayinfo()
product1.addtax(.08)
product1.takeback("Defective").displayinfo()