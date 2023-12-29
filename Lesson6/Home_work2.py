class Road:
    def __init__(self, length, width ):
        self.length=length
        self.width=width

road_instance = Road(length=1000, width=10)

print(f"Длина дороги: {road_instance.length} метров")
print(f"Ширина дороги: {road_instance.width} метров")

# масса асфальта для покрытия одного кв метра дороги асфальтом
weight=int(input("Масса асфальта: "))

# Толшина
thickness=int(input("Толшина асвальта: "))
mass_calc_method= road_instance.length*road_instance.width*weight*thickness
print(f"Метод расчета массы асфальта для покрытия всего дорожного полотна: {mass_calc_method} тон")