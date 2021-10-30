from dc_va_settings import *
from relays import *




class DC_VA:
    def __init__(self, relay_ip, relay_port, relay_password, state):
        self.__connector = RelayConnector(relay_ip, relay_port, relay_password)
        self.__group = RelaysGroup(['C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21', 'C22', 'C23', 'C24', 'C25'], self.__connector)
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
            'V_IN10' : self.__group.configure("V_IN10", DC_VA_Settings.conf_dict_v_in_10),
            'V_IN11' : self.__group.configure("V_IN11", DC_VA_Settings.conf_dict_v_in_11),
            'V_IN12' : self.__group.configure("V_IN12", DC_VA_Settings.conf_dict_v_in_12),
            'A_IN1' : self.__group.configure("A_IN1", DC_VA_Settings.conf_dict_a_in_1),
            'A_IN2' : self.__group.configure("A_IN2", DC_VA_Settings.conf_dict_a_in_2)
        }

        self.__initialize()

        self.__state = state
        self.__relay = self.__states[state]
        self.__relay(state)

    def invertState(self):
        self.__relay(self.__state)

    def changeState(self, arg):
        self.__relay(arg)

    def getVoltage(self, index):
        voltage = -1
        if index == 1:
            voltage = DC_VA_Settings.instrument.read_register(registeraddress=DC_VA_Settings.VOLT_1, functioncode=4, signed=True)

        if index == 2:
            voltage = DC_VA_Settings.instrument.read_register(registeraddress=DC_VA_Settings.VOLT_2, functioncode=4, signed=True)

        return voltage

    def getAmperage(self, index):
        amperage = -1
        if index == 1:
            amperage = DC_VA_Settings.instrument.read_register(registeraddress=DC_VA_Settings.AMP_1, functioncode=4, signed=True)

        if index == 2:
            amperage = DC_VA_Settings.instrument.read_register(registeraddress=DC_VA_Settings.AMP_2, functioncode=4, signed=True)

        return amperage

    def __initialize(self):
        self.__states['V_IN1']('V_IN1')
        self.__states['V_IN11']('V_IN11')
        self.__states['A_IN1']('A_IN1')

    def __del__(self):
        if self.__connector:
            self.__connector.deinitConnection()
