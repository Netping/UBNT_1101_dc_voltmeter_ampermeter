#!/usr/bin/python3
from dc_va import *




def main():
    SuperCapVoltage = DC_VA('192.168.0.101', 2424, 'Laurent', 'V_IN7')
    print("Voltage1: " + SuperCapVoltage.getVoltage(1))
    print("Voltage2: " + SuperCapVoltage.getVoltage(2))
    print("Amperage1: " + SuperCapVoltage.getAmperage(1))
    print("Amperage2: " + SuperCapVoltage.getAmperage(2))

if __name__ == "__main__":
    main()
