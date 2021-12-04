from dc_va_settings import *
from relays import *
import time




WAIT_TIME = 4
GROUP = ['C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21', 'C22', 'C23', 'C24', 'C25']

class DC_VA_IN1_TO_IN10:
    def __init__(self):
        self.__group = RelaysGroup(GROUP)
        self.__states = {
            'V_IN1'  : self.__group.configure("V_IN1", DC_VA_Settings.conf_dict_v_in_1),
            'V_IN2'  : self.__group.configure("V_IN2", DC_VA_Settings.conf_dict_v_in_2),
            'V_IN3'  : self.__group.configure("V_IN3", DC_VA_Settings.conf_dict_v_in_3),
            'V_IN4'  : self.__group.configure("V_IN4", DC_VA_Settings.conf_dict_v_in_4),
            'V_IN5'  : self.__group.configure("V_IN5", DC_VA_Settings.conf_dict_v_in_5),
            'V_IN6'  : self.__group.configure("V_IN6", DC_VA_Settings.conf_dict_v_in_6),
            'V_IN7'  : self.__group.configure("V_IN7", DC_VA_Settings.conf_dict_v_in_7),
            'V_IN8'  : self.__group.configure("V_IN8", DC_VA_Settings.conf_dict_v_in_8),
            'V_IN9'  : self.__group.configure("V_IN9", DC_VA_Settings.conf_dict_v_in_9),
            'V_IN10' : self.__group.configure("V_IN10", DC_VA_Settings.conf_dict_v_in_10)
        }

        self.__relay = None
        self.connect('OFF')

    def connect(self, channel):
        if self.__relay:
            self.__relay('OFF')

        if channel.upper() != 'OFF':
            if self.__relay:
                self.__relay('OFF')

            self.__relay = self.__states[channel]
            self.__relay('ON')

            time.sleep(WAIT_TIME)

    def getVoltage(self):
        voltage = DC_VA_Settings.instrument.read_register(registeraddress=DC_VA_Settings.VOLT_1, functioncode=4, signed=True)

        return voltage

class DC_VA_11:
    def __init__(self):
        self.__group = RelaysGroup(GROUP)
        self.__relay = self.__group.configure("V_IN11", DC_VA_Settings.conf_dict_v_in_11)
        self.__relay('ON')

        time.sleep(WAIT_TIME)

    def getVoltage(self):
        voltage = DC_VA_Settings.instrument.read_register(registeraddress=DC_VA_Settings.VOLT_1, functioncode=4, signed=True)

        return voltage

class DC_A_IN1:
    def __init__(self):
        self.__group = RelaysGroup(GROUP)
        self.__relay = self.__group.configure("A_IN1", DC_VA_Settings.conf_dict_a_in_1)
        self.__relay('ON')

        time.sleep(WAIT_TIME)

    def getAmperage(self):
        amperage = DC_VA_Settings.instrument.read_register(registeraddress=DC_VA_Settings.AMP_1, functioncode=4, signed=True)

        return amperage

class DC_A_IN2:
    def __init__(self):
        self.__group = RelaysGroup(GROUP)
        self.__relay = self.__group.configure("A_IN2", DC_VA_Settings.conf_dict_a_in_2)
        self.__relay('ON')

        time.sleep(WAIT_TIME)

    def getAmperage(self):
        amperage = DC_VA_Settings.instrument.read_register(registeraddress=DC_VA_Settings.AMP_1, functioncode=4, signed=True)

        return amperage
