from Location import Location


class Node:

    def __init__(self, key, loc):
        self.id = key
        self.location = loc
        self.tag = 0
        self.info = ""
        self.weight = 0

    def location_toString(self):
        return f"{self.loc[0]},{self.loc[1]},{self.loc[2]}"
