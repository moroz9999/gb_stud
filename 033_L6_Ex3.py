class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._incom = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)
        
    def get_total_income(self):
        print(self._incom.get('wage') + self._incom.get('bonus'))

emp = [Position('Serguey', 'Ivanov', 'accauntant', 70000, 20000), 
       Position('Andrew', 'Vodkin', 'engeneer', 85000, 18000)]
for i in emp:
    i.get_full_name()
    i.get_total_income()
    print()
