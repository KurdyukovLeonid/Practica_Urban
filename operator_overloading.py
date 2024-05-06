class Building:

    def __init__(self):
        self.numberOfFloors = 5
        self.buildingType = 'stone'

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors
        return self.buildingType == other.buildingType

build = Building
build.__eq__()