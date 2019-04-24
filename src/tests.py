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
        self.assertEqual(Parkinglotobj.createSpace(6),"Created a parking lot with 6 slots", "Should be 6") 

                         
if __name__ == '__main__':
    unittest.main()

