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

    def freeSlot(self,slotId):
        if slotId < (self.capacity) :
            if self.slot[slotId-1]==None:
                return("slot is already free")
            else:
                self.slot[slotId-1]=None
                return "Slot number "+str(slotId)+" is free"
            
        elif self.capacity ==0:
            return "Parking lot doesnot have "+str(slotId)
    
    def status(self):
        string="Slot No.   Registration_No   Colour"
        for members in range(0,self.capacity):
            if self.slot[members]!=None:
                string=string+"\n"+"   "+str(members+1)+"       "+str(self.slot[members].RegestrationNo)+"       "+str(self.slot[members].color)
        return string

    def registerNo_ofColor(self,color):
        stringofregisterNo=""
        for members in range(0,self.capacity):
            if self.slot[members]!= None and self.slot[members].color==color :
                stringofregisterNo=stringofregisterNo+str(self.slot[members].RegestrationNo)+","
        if len(stringofregisterNo)==0:
            return "no vehicle found"
        return stringofregisterNo[:-1]

    def slotOf_registerNo(self,RegestrationNo):
        Found=False
        for members in range(0,self.capacity):
            if self.slot[members]!= None and self.slot[members].RegestrationNo==RegestrationNo :
                Found=True
                return str(members+1)        
        if Found== False:
            return "Not Found"
        
    def slotsOf_rcolor(self,color):
        stringofregisterNo=""
        for members in range(0,self.capacity):
            if self.slot[members]!= None and self.slot[members].color==color :
                stringofregisterNo=stringofregisterNo+str(members+1)+","
        if len(stringofregisterNo)==0:
            return "no slot found"
        return stringofregisterNo[:-1]