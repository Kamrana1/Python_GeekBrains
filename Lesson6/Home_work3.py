class Worker:
    def __init__(self,name, surname, position, wage, bonus ):
        self.income = {"wage": wage, "bonus": bonus}
        self.position = position
        self.surname = surname
        self.name = name
        self.wage = wage
        self.bonus = bonus

class Position(Worker):

    def __init__(self,name, surname, position, wage, bonus ):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self, worker):
        print(f"{self.name} {self.surname}")

    def get_total_income(self,worker):
        print(f"Salary+bonus {self.wage+self.bonus}")


worker = Worker("Kamran","Aliyev","Direktor", 5000, 3000)

position=Position("Kamran","Aliyev","Direktor", 5000, 3000)

position.get_full_name(worker)
position.get_total_income(worker)
