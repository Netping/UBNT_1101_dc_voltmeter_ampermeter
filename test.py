#!/usr/bin/python3
from dc_va import *
import time




def main():
    SuperCapVoltage = DC_VA('192.168.1.101', 2425, 'Laurent', 'V_IN1')
    time.sleep(4)
    print("Voltage1: ", SuperCapVoltage.getVoltage(1))
    print("Voltage2: ", SuperCapVoltage.getVoltage(2))
    print("Amperage1: ", SuperCapVoltage.getAmperage(1))
    print("Amperage2: ", SuperCapVoltage.getAmperage(2))

if __name__ == "__main__":
    main()
