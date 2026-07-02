class cars:
    def __init__(self, car, model):
        self.car_name = car
        self.model = model

    def display_car(self):
        print(f"Your car is {self.car_name}, {self.model}")

print("Enter car details: ")
car_name = input("Car name: ")
car_model = input("Car model: ")
car1 = cars(car_name, car_model)
cars.display_car(car1)