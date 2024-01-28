class Expand_territory:
    def __init__(self):
        self.territory = []

    def add_land(self, land):
        self.territory.append(land)

    def acquire_territory(self, new_territory):
        self.territory.extend(new_territory)

    def remove_land(self, land):
        self.territory.remove(land)

    def increase_territory(self, percentage):
        increase_amount = int(len(self.territory) * (percentage / 100))
        self.territory += [None] * increase_amount

expand_territory = Expand_territory()