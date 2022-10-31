class Cars:
    def __init__ (self, name, price, type):
        self.name = name
        self.price = price
        self.type = type

Car_1 = Cars ("Pugo", "10 lakhs", "Red Convertible")
Car_2 = Cars ("Mavo", "6 lakhs", "Blue Sedan")

print(Car_1.name)
print(Car_2.name)

