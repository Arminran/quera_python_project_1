class WorkPlaceIsFull(Exception):
    def __str__(self):
        return "work place is full!"


class Consts:
    BASE_PRICE = {'mine': 150, 'school': 100, 'company': 90}
    BASE_PLACE_COST = 2500
    LEVEL_MUL = 50

def hire(self, person) -> None:
    if len(self.employees) >= self.capacity:
        raise WorkPlaceIsFull()
    self.employees.append(person)
    person.work_place = self
class WorkPlace:
    instances = []
    def __init__(self, name: str) -> None:
        self.name = name
        self.level = 1
        self.expertise = ""
        self.employees = [] 
        self.capacity = 1
        WorkPlace.instances.append(self)

    def get_price(self) -> int:
        takhasos = self.expertise
        return Consts.BASE_PRICE[takhasos]

    def calc_costs(self):
        pass

    def calc_capacity(self):
        pass

    def upgrade(self) -> None:
        self.level = self.level + 1
        self.calc_capacity()

    def hire(self, person) -> None:
        if self.calc_capacity() <= len(self.employees) :
            raise WorkPlaceIsFull()
        else :
            self.employees.append(person)
            person.work_place = self

    def get_expertise(self) -> str:
        return self.expertise

    def calc(self) -> int:
        return -(self.calc_costs())

    @staticmethod
    def calc_all() -> int:
        sum = 0
        for workplace in WorkPlace.instances :
            sum += workplace.calc()

        return sum