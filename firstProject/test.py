class car:
    def __init__(self,brand,colour):
        self.brand=brand
        self.colour=colour

    def show_details(self):
        print("Car Brand is:", self.brand, "& Car colour is:",self.colour)

car1=car("Tata","Red")
car2=car("Ford","Black")

car1.show_details()
car2.show_details()

