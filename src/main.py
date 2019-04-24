#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    Created on Tue Apr 23 14:26:27 2019
    
    @author: Nikhil.g
    """

import sys
from vehicle import vehicle
from Parkinglot import Parkinglot

def commandLine(line,parkinglotObj):
    parkinglotObj=parkinglotObj
    commands=line.rstrip("\n").split(" ")
    if len(commands)==2 and str(commands[0])=="create_parking_lot":
        return parkinglotObj.createSpace(int(commands[1]))
    elif len(commands)==1 and str(commands[0])=="status":
        return parkinglotObj.status()
    elif len(commands)==2 and str(commands[0])=="leave":
        return parkinglotObj.freeSlot(int(commands[1]))
    elif len(commands)==3 and str(commands[0])=="park":
        vehicleobj=vehicle(str(commands[1]),str(commands[2]))
        return parkinglotObj.slotAllot(vehicleobj)
    elif len(commands)==2 and str(commands[0])=="slot_number_for_registration_number":
        return parkinglotObj.slotOf_registerNo(str(commands[1]))
    elif len(commands)==2 and str(commands[0])=="slot_numbers_for_cars_with_colour":
        return parkinglotObj.slotsOf_rcolor(str(commands[1]))
    elif len(commands)==2 and str(commands[0])=="registration_numbers_for_cars_with_colour":
        return parkinglotObj.registerNo_ofColor(str(commands[1]))
    else:
        
        return "please check the input given."+"You typed :"+commands[0]


if __name__ == '__main__':
    parkinglotObj=Parkinglot()
    if len(sys.argv) ==3:
        with open(r"../data//"+str(sys.argv[2]),"r") as f:
            lines=f.readlines()
            for line in lines:
                print(commandLine(str(line),parkinglotObj))
    elif len(sys.argv) ==2:
        while(1):
            line=str(input("#"))
            if line=="exit":
                break
            print(commandLine(line,parkinglotObj))
        

