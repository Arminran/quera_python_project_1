from work_place import WorkPlace, Consts


class Mine(WorkPlace):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.expertise = "mine"

    def calc_capacity(self) -> None:
        self.capacity = self.level * self.level 
    
    def calc_costs(self):
        return (Consts.LEVEL_MUL*self.level)+Consts.BASE_PLACE_COST