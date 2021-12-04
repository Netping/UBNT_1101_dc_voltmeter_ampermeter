#!/usr/bin/python3
from dc_va import *
import time




def main():
    SuperCapVoltage = DC_VA_IN1_TO_IN10()
    SuperCapVoltage.connect("V_IN1")

    SuperCapAmperage = DC_A_IN1()

    print("Voltage: ", SuperCapVoltage.getVoltage())
    print("Amperage: ", SuperCapAmperage.getAmperage())

if __name__ == "__main__":
    main()
