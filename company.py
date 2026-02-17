from work_place import WorkPlace, Consts


class Company(WorkPlace):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.expertise = "company"

    def calc_capacity(self) -> None:
        self.capacity = self.level

    def calc_costs(self) -> int:
        lev = 0
        if self.level < 0 :
            lev = self.level * -1
        else :
            lev = self.level
        costs = Consts.BASE_PLACE_COST * lev
        return costs