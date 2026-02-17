from work_place import WorkPlace, Consts
import math


class School(WorkPlace):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.expertise = "school"

    def calc_capacity(self) -> None:
         self.capacity = math.floor(math.sqrt(self.level))

    def calc_costs(self) -> int:
        lev = 0
        if self.level < 0 :
            lev = self.level * -1
        else :
            lev = self.level
        costs = Consts.BASE_PLACE_COST * math.floor(math.sqrt(lev))
        return costs