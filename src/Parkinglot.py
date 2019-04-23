from vehicle import vehicle


class Parkinglot:
    def __init__(self,capacity=0):
        self.capacity=capacity
        self.slot = [None]*capacity
        print("Initilazing Parking Space")
