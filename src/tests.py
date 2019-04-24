from vehicle import vehicle
from Parkinglot import Parkinglot
import unittest


class TestSum(unittest.TestCase):
    
    def test_vehicle_class(self):
        vehicleobj=vehicle('KA-01-HH-1234','red')
        self.assertEqual(vehicleobj.RegestrationNo,'KA-01-HH-1234', "Should be KA-01-HH-1234")
    
    def test_Parkinglot_capacity(self):
        Parkinglotobj=Parkinglot()
        self.assertEqual(Parkinglotobj.capacity,0, "Should be 0")

    def test_Parkinglot_createSpace(self):
        Parkinglotobj=Parkinglot()
        self.assertEqual(Parkinglotobj.createSpace(6),"Created a parking lot with 6 slots", "Should be Created a parking lot with 6 slots")
        
    def test1_Parkinglot_slotAllot(self):
        vehicleobj=vehicle('KA-01-HH-1234','red')
        Parkinglotobj=Parkinglot()
        string=Parkinglotobj.slotAllot(vehicleobj)
        self.assertEqual(string,"Sorry, parking lot is full", "Should be Sorry, parking lot is full")         
        
    def test2_Parkinglot_slotAllot(self):
        vehicleobj=vehicle('KA-01-HH-1234','red')
        Parkinglotobj=Parkinglot()       
        Parkinglotobj.createSpace(6)
        string=Parkinglotobj.slotAllot(vehicleobj)
        self.assertEqual(string,"Allocated slot number: 1", "Should be Allocated slot number: 1")  
        
    def test1_Parkinglot_freeSlot1(self):
        Parkinglotobj=Parkinglot()
        string=Parkinglotobj.freeSlot(0)
        self.assertEqual(string,"Parking lot doesnot have 0", "Should be Parking lot doesnot have 0")  

    def test1_Parkinglot_freeSlot2(self):
        vehicleobj=vehicle('KA-01-HH-1234','red')
        Parkinglotobj=Parkinglot()
        Parkinglotobj.createSpace(6)
        string=Parkinglotobj.slotAllot(vehicleobj)
        string=Parkinglotobj.freeSlot(1)
        self.assertEqual(string,"Slot number 1 is free", "Should be Slot number 1 is free") 
        
    def test2_Parkinglot_freeSlot3(self):
        vehicleobj=vehicle('KA-01-HH-1234','red')
        Parkinglotobj=Parkinglot()
        Parkinglotobj.createSpace(6)
        string=Parkinglotobj.slotAllot(vehicleobj)
        string=Parkinglotobj.freeSlot(2)
        self.assertEqual(string,"slot is already free", "Should be slot is already free") 

    def test_Parkinglot_status1(self):
        Parkinglotobj=Parkinglot()
        self.assertEqual(Parkinglotobj.status(),"Slot No.   Registration_No   Colour", "Should be Slot No.   Registration_No   Colour")

    def test_Parkinglot_status2(self):
        vehicleobj=vehicle('KA-01-HH-1234','red')
        Parkinglotobj=Parkinglot()
        Parkinglotobj.createSpace(6)
        Parkinglotobj.slotAllot(vehicleobj)
        self.assertEqual(Parkinglotobj.status(),"Slot No.   Registration_No   Colour"+"\n"+"   "+"1"+"       "+"KA-01-HH-1234"+"       "+"red", "Should be Slot No.   Registration_No   Colour")

    def test_Parkinglot_registerNo_ofColor1(self):
        Parkinglotobj=Parkinglot()
        self.assertEqual(Parkinglotobj.registerNo_ofColor('red'),"no vehicle found", "Should be no vehicle found")
        
    def test_Parkinglot_registerNo_ofColor2(self):
        vehicleobj=vehicle('KA-01-HH-1234','red')
        Parkinglotobj=Parkinglot()
        Parkinglotobj.createSpace(6)
        Parkinglotobj.slotAllot(vehicleobj)        
        self.assertEqual(Parkinglotobj.registerNo_ofColor('red'),"KA-01-HH-1234", "Should be KA-01-HH-1234")

    def test_Parkinglot_registerNo_ofColor3(self):
        vehicleobj=vehicle('KA-01-HH-1234','red')
        Parkinglotobj=Parkinglot()
        Parkinglotobj.createSpace(6)
        Parkinglotobj.slotAllot(vehicleobj)        
        self.assertEqual(Parkinglotobj.registerNo_ofColor('white'),"no vehicle found", "Should be no vehicle found")
        
if __name__ == '__main__':
    unittest.main()

