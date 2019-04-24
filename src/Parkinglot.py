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

    def slotAllot(self,vehicle):
        flag=True
        for members in range(0,self.capacity):
            if self.slot[members]==None:
                self.slot[members] = vehicle
                flag=False
                return "Allocated slot number: "+str(members+1)
                break
        if flag:
            return "Sorry, parking lot is full"