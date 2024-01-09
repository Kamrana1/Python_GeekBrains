class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("The car is moving.")

    def stop(self):
        print("The car has stopped.")

    def turn(self, direction):
        print(f"The car turned {direction}.")

    def show_speed(self):
        print(f"Current speed: {self.speed} km/h")

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Warning: Speed limit exceeded!")

class SportCar(Car):
    pass  # Мы можем использовать атрибуты и методы из базового класса Car

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Warning: Speed limit exceeded!")

class PoliceCar(Car):
    pass  # Мы можем использовать атрибуты и методы из базового класса Car

# Пример использования классов
town_car = TownCar(speed=70, color='blue', name='CityCar', is_police=False)
sport_car = SportCar(speed=120, color='red', name='Ferrari', is_police=False)
work_car = WorkCar(speed=45, color='white', name='Truck', is_police=False)
police_car = PoliceCar(speed=80, color='black', name='PoliceCar', is_police=True)

town_car.show_speed()
sport_car.show_speed()
work_car.show_speed()
police_car.show_speed()