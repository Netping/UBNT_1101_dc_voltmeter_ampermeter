import minimalmodbus




class DC_VA_Settings:
    PORT = '/dev/dkst1101/COM19'
    MODBUS_ADDRESS = 8
    VOLT_1 = 0x2
    VOLT_2 = 0x3
    AMP_1 = 0x8
    AMP_2 = 0x9

    instrument = minimalmodbus.Instrument(PORT, MODBUS_ADDRESS, mode=minimalmodbus.MODE_RTU)

    instrument.serial.baudrate = 9600        # Baud
    instrument.serial.bytesize = 8
    instrument.serial.parity   = minimalmodbus.serial.PARITY_NONE
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

    conf_dict_v_in_11 = {
            'ON' : [
                        {
                            'name' : 'C14',
                            'state' : 'OFF'
                        },
                        {
                            'name' : 'C15',
                            'state' : 'OFF'
                        }
                    ],

            'OFF' : all_off
        }

    conf_dict_v_in_12 = {
            'ON' : [
                        {
                            'name' : 'C14',
                            'state' : 'ON'
                        },
                        {
                            'name' : 'C15',
                            'state' : 'ON'
                        }
                    ],

            'OFF' : all_off
        }

    conf_dict_a_in_1 = {
            'ON' : [
                        {
                            'name' : 'C12',
                            'state' : 'OFF'
                        },
                        {
                            'name' : 'C13',
                            'state' : 'OFF'
                        }
                    ],

            'OFF' : all_off
        }

    conf_dict_a_in_2 = {
            'ON' : [
                        {
                            'name' : 'C12',
                            'state' : 'ON'
                        },
                        {
                            'name' : 'C13',
                            'state' : 'ON'
                        }
                    ],

            'OFF' : all_off
        }
