#!/usr/bin/python3
import minimalmodbus
from relays import *




PORT = '/dev/dkst1101/COM19'
MODBUS_ADDRESS = 8
REGISTER_1 = 100

instrument = minimalmodbus.Instrument(PORT, MODBUS_ADDRESS, mode=minimalmodbus.MODE_RTU)

instrument.serial.baudrate = 19200        # Baud
instrument.serial.bytesize = 8
instrument.serial.parity   = minimalmodbus.serial.PARITY_EVEN
instrument.serial.stopbits = 1
instrument.serial.timeout  = 1

instrument.close_port_after_each_call = True
instrument.clear_buffers_before_each_transaction = True

#relays
all_off = [
                    {
                        'name' : 'C16',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C17',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C18',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C19',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C20',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C21',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C22',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C23',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C24',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C25',
                        'state' : 'OFF'
                    }
            ]

conf_dict_v_in_1 = {
        'ON' : [
                    {
                        'name' : 'C16',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C17',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C18',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C19',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C20',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C21',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C22',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C23',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C24',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C25',
                        'state' : 'ON'
                    }
                ],

        'OFF' : all_off
    }

conf_dict_v_in_2 = {
        'ON' : [
                    {
                        'name' : 'C16',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C17',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C18',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C19',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C20',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C21',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C22',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C23',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C24',
                        'state' : 'ON'
                    },
                    {
                        'name' : 'C25',
                        'state' : 'OFF'
                    }
                ],

        'OFF' : all_off
    }

conf_dict_v_in_3 = {
        'ON' : [
                    {
                        'name' : 'C16',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C17',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C18',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C19',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C20',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C21',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C22',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C23',
                        'state' : 'ON'
                    },
                    {
                        'name' : 'C24',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C25',
                        'state' : 'OFF'
                    }
                ],

        'OFF' : all_off
    }

conf_dict_v_in_4 = {
        'ON' : [
                    {
                        'name' : 'C16',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C17',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C18',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C19',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C20',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C21',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C22',
                        'state' : 'ON'
                    },
                    {
                        'name' : 'C23',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C24',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C25',
                        'state' : 'OFF'
                    }
                ],

        'OFF' : all_off
    }

conf_dict_v_in_5 = {
        'ON' : [
                    {
                        'name' : 'C16',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C17',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C18',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C19',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C20',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C21',
                        'state' : 'ON'
                    },
                    {
                        'name' : 'C22',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C23',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C24',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C25',
                        'state' : 'OFF'
                    }
                ],

        'OFF' : all_off
    }

conf_dict_v_in_6 = {
        'ON' : [
                    {
                        'name' : 'C16',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C17',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C18',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C19',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C20',
                        'state' : 'ON'
                    },
                    {
                        'name' : 'C21',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C22',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C23',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C24',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C25',
                        'state' : 'OFF'
                    }
                ],

        'OFF' : all_off
    }

conf_dict_v_in_7 = {
        'ON' : [
                    {
                        'name' : 'C16',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C17',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C18',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C19',
                        'state' : 'ON'
                    },
                    {
                        'name' : 'C20',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C21',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C22',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C23',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C24',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C25',
                        'state' : 'OFF'
                    }
                ],

        'OFF' : all_off
    }

conf_dict_v_in_8 = {
        'ON' : [
                    {
                        'name' : 'C16',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C17',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C18',
                        'state' : 'ON'
                    },
                    {
                        'name' : 'C19',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C20',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C21',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C22',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C23',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C24',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C25',
                        'state' : 'OFF'
                    }
                ],

        'OFF' : all_off
    }

conf_dict_v_in_9 = {
        'ON' : [
                    {
                        'name' : 'C16',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C17',
                        'state' : 'ON'
                    },
                    {
                        'name' : 'C18',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C19',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C20',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C21',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C22',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C23',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C24',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C25',
                        'state' : 'OFF'
                    }
                ],

        'OFF' : all_off
    }

conf_dict_v_in_10 = {
        'ON' : [
                    {
                        'name' : 'C16',
                        'state' : 'ON'
                    },
                    {
                        'name' : 'C17',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C18',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C19',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C20',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C21',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C22',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C23',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C24',
                        'state' : 'OFF'
                    },
                    {
                        'name' : 'C25',
                        'state' : 'OFF'
                    }
                ],

        'OFF' : all_off
    }

connector = RelayConnector('192.168.0.101', 2424, 'Laurent')

group = RelaysGroup(['C16', 'C17', 'C18', 'C19', 'C20', 'C21', 'C22', 'C23', 'C24', 'C25'], connector)

V_IN1 = group.configure("V_IN1", conf_dict_v_in_1)
V_IN2 = group.configure("V_IN2", conf_dict_v_in_2)
V_IN3 = group.configure("V_IN3", conf_dict_v_in_3)
V_IN4 = group.configure("V_IN4", conf_dict_v_in_4)
V_IN5 = group.configure("V_IN5", conf_dict_v_in_5)
V_IN6 = group.configure("V_IN6", conf_dict_v_in_6)
V_IN7 = group.configure("V_IN7", conf_dict_v_in_7)
V_IN8 = group.configure("V_IN8", conf_dict_v_in_8)
V_IN9 = group.configure("V_IN9", conf_dict_v_in_9)
V_IN10 = group.configure("V_IN10", conf_dict_v_in_10)


V_IN1('V_IN1')

#TODO read from modbus

connector.deinitConnection()
