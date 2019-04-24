from vehicle import vehicle


class Parkinglot:
    def __init__(self):
        self.capacity=0
        self.slot = [None]*self.capacity
        print("Initilazing Parking Space")
    
    def createSpace(self,capacity=0):
        self.capacity=capacity
        self.slot = [None]*capacity
        return "Created a parking lot with "+str(self.capacity)+" slots"
