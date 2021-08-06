from homeassistant.components.sensor import (
    STATE_CLASS_MEASUREMENT,
)
from homeassistant.const import (
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_POWER_FACTOR,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_VOLTAGE,
)


DOMAIN = "saj_modbus"
DEFAULT_NAME = "SAJ"
DEFAULT_SCAN_INTERVAL = 60
DEFAULT_PORT = 502
CONF_SAJ_HUB = "saj_hub"
ATTR_MANUFACTURER = "SAJ Electric"

SENSOR_TYPES = {
    "DevType": ["Device Type", "devtype", None, "mdi:information-outline", None],
    "SubType": ["Sub Type", "subtype", None, "mdi:information-outline", None],
    "CommVer": [
        "Comms Protocol Version",
        "commver",
        None,
        "mdi:information-outline",
        None,
    ],
    "SN": ["Serial Number", "sn", None, "mdi:information-outline", None],
    "PC": ["Product Code", "pc", None, "mdi:information-outline", None],
    "DV": ["Display Software Version", "dv", None, "mdi:information-outline", None],
    "MCV": [
        "Master Ctrl Software Version",
        "mcv",
        None,
        "mdi:information-outline",
        None,
    ],
    "SCV": [
        "Slave Ctrl Software Version",
        "scv",
        None,
        "mdi:information-outline",
        None,
    ],
    "DispHWVersion": [
        "Display Board Hardware Version",
        "disphwversion",
        None,
        "mdi:information-outline",
        None,
    ],
    "CtrlHWVersion": [
        "Control Board Hardware Version",
        "ctrlhwversion",
        None,
        "mdi:information-outline",
        None,
    ],
    "PowerHWVersion": [
        "Power Board Hardware Version",
        "powerhwversion",
        None,
        "mdi:information-outline",
        None,
    ],
    "MPVStatus": [
        "Inverter status",
        "mpvstatus",
        None,
        "mdi:information-outline",
        None,
    ],
    "MPVMode": [
        "Inverter working mode",
        "mpvmode",
        None,
        "mdi:information-outline",
        None,
    ],
    "FaultMSG": [
        "Inverter error message",
        "faultmsg",
        None,
        "mdi:message-alert-outline",
        None,
    ],
    "PV1Volt": [
        "PV1 voltage",
        "pv1volt",
        "V",
        None,
        DEVICE_CLASS_VOLTAGE,
        STATE_CLASS_MEASUREMENT,
    ],
    "PV1Curr": [
        "PV1 total current",
        "pv1curr",
        "A",
        "mdi:current-ac",
        DEVICE_CLASS_CURRENT,
        STATE_CLASS_MEASUREMENT,
    ],
    "PV1Power": [
        "PV1 power",
        "pv1power",
        "W",
        "mdi:solar-power",
        DEVICE_CLASS_POWER,
        STATE_CLASS_MEASUREMENT,
    ],
    "PV2Volt": [
        "PV2 voltage",
        "pv2volt",
        "V",
        None,
        DEVICE_CLASS_VOLTAGE,
        STATE_CLASS_MEASUREMENT,
    ],
    "PV2Curr": [
        "PV2 total current",
        "pv2curr",
        "A",
        "mdi:current-ac",
        DEVICE_CLASS_CURRENT,
        STATE_CLASS_MEASUREMENT,
    ],
    "PV2Power": [
        "PV2 power",
        "pv2power",
        "W",
        "mdi:solar-power",
        DEVICE_CLASS_POWER,
        STATE_CLASS_MEASUREMENT,
    ],
    "PV3Volt": [
        "PV3 voltage",
        "pv3volt",
        "V",
        None,
        DEVICE_CLASS_VOLTAGE,
        STATE_CLASS_MEASUREMENT,
    ],
    "PV3Curr": [
        "PV3 total current",
        "pv3curr",
        "A",
        "mdi:current-ac",
        DEVICE_CLASS_CURRENT,
        STATE_CLASS_MEASUREMENT,
    ],
    "PV3Power": ["PV3 power", "pv3power", "W", "mdi:solar-power", DEVICE_CLASS_POWER],
    "BusVolt": ["BUS voltage", "busvolt", "V", None, DEVICE_CLASS_VOLTAGE],
    "InvTempC": [
        "Inverter temperature",
        "invtempc",
        "°C",
        None,
        DEVICE_CLASS_TEMPERATURE,
        STATE_CLASS_MEASUREMENT,
    ],
    "GFCI": ["GFCI", "gfci", "mA", "mdi:current-dc", DEVICE_CLASS_CURRENT],
    "Power": [
        "Active power of inverter total output",
        "power",
        "W",
        "mdi:solar-power",
        DEVICE_CLASS_POWER,
        STATE_CLASS_MEASUREMENT,
    ],
    "QPower": [
        "Reactive power of inverter total output",
        "qpower",
        "VAR",
        "mdi:flash",
        None,
    ],
    "PF": [
        "Total power factor of inverter",
        "pf",
        None,
        None,
        DEVICE_CLASS_POWER_FACTOR,
    ],
    "L1Volt": [
        "L1 voltage",
        "l1volt",
        "V",
        None,
        DEVICE_CLASS_VOLTAGE,
        STATE_CLASS_MEASUREMENT,
    ],
    "L1Curr": [
        "L1 current",
        "l1curr",
        "A",
        "mdi:current-ac",
        DEVICE_CLASS_CURRENT,
        STATE_CLASS_MEASUREMENT,
    ],
    "L1Freq": ["L1 frequency", "l1freq", "Hz", "mdi:sine-wave", None],
    "L1DCI": [
        "L1 DC component",
        "l1dci",
        "mA",
        "mdi:current-dc",
        DEVICE_CLASS_CURRENT,
        STATE_CLASS_MEASUREMENT,
    ],
    "L1Power": [
        "L1 power",
        "l1power",
        "W",
        "mdi:solar-power",
        DEVICE_CLASS_POWER,
        STATE_CLASS_MEASUREMENT,
    ],
    "L1PF": [
        "L1 power factor",
        "l1pf",
        None,
        None,
        DEVICE_CLASS_POWER_FACTOR,
        STATE_CLASS_MEASUREMENT,
    ],
    "L2Volt": [
        "L2 voltage",
        "l2volt",
        "V",
        None,
        DEVICE_CLASS_VOLTAGE,
        STATE_CLASS_MEASUREMENT,
    ],
    "L2Curr": [
        "L2 current",
        "l2curr",
        "A",
        "mdi:current-ac",
        DEVICE_CLASS_CURRENT,
        STATE_CLASS_MEASUREMENT,
    ],
    "L2Freq": ["L2 frequency", "l2freq", "Hz", "mdi:sine-wave", None],
    "L2DCI": [
        "L2 DC component",
        "l2dci",
        "mA",
        "mdi:current-dc",
        DEVICE_CLASS_CURRENT,
        STATE_CLASS_MEASUREMENT,
    ],
    "L2Power": [
        "L2 power",
        "l2power",
        "W",
        "mdi:solar-power",
        DEVICE_CLASS_POWER,
        STATE_CLASS_MEASUREMENT,
    ],
    "L2PF": [
        "L2 power factor",
        "l2pf",
        None,
        None,
        DEVICE_CLASS_POWER_FACTOR,
        STATE_CLASS_MEASUREMENT,
    ],
    "L3Volt": [
        "L3 voltage",
        "l3volt",
        "V",
        None,
        DEVICE_CLASS_VOLTAGE,
        STATE_CLASS_MEASUREMENT,
    ],
    "L3Curr": [
        "L3 current",
        "l3curr",
        "A",
        "mdi:current-ac",
        DEVICE_CLASS_CURRENT,
        STATE_CLASS_MEASUREMENT,
    ],
    "L3Freq": ["L3 frequency", "l3freq", "Hz", "mdi:sine-wave", None],
    "L3DCI": [
        "L3 DC component",
        "l3dci",
        "mA",
        "mdi:current-dc",
        DEVICE_CLASS_CURRENT,
        STATE_CLASS_MEASUREMENT,
    ],
    "L3Power": [
        "L3 power",
        "l3power",
        "W",
        "mdi:solar-power",
        DEVICE_CLASS_POWER,
        STATE_CLASS_MEASUREMENT,
    ],
    "L3PF": [
        "L3 power factor",
        "l3pf",
        None,
        None,
        DEVICE_CLASS_POWER_FACTOR,
        STATE_CLASS_MEASUREMENT,
    ],
    "ISO1": ["PV1+_ISO", "iso1", "kΩ", "mdi:omega", None],
    "ISO2": ["PV2+_ISO", "iso2", "kΩ", "mdi:omega", None],
    "ISO3": ["PV3+_ISO", "iso3", "kΩ", "mdi:omega", None],
    "ISO4": ["PV__ISO", "iso4", "kΩ", "mdi:omega", None],
    "TodayEnergy": [
        "Power generation on current day",
        "todayenergy",
        "kWh",
        "mdi:solar-power",
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_MEASUREMENT,
        "today",
    ],
    "MonthEnergy": [
        "Power generation in current month",
        "monthenergy",
        "kWh",
        "mdi:solar-power",
        DEVICE_CLASS_ENERGY,
    ],
    "YearEnergy": [
        "Power generation in current year",
        "yearenergy",
        "kWh",
        "mdi:solar-power",
        DEVICE_CLASS_ENERGY,
    ],
    "TotalEnergy": [
        "Total power generation",
        "totalenergy",
        "kWh",
        "mdi:solar-power",
        DEVICE_CLASS_ENERGY,
        STATE_CLASS_MEASUREMENT,
        True,
    ],
    "TodayHour": [
        "Daily working hours",
        "todayhour",
        "h",
        "mdi:progress-clock",
        None,
        STATE_CLASS_MEASUREMENT,
        "today",
    ],
    "TotalHour": [
        "Total working hours",
        "totalhour",
        "h",
        "mdi:progress-clock",
        None,
        STATE_CLASS_MEASUREMENT,
        True,
    ],
    "ErrorCount": ["Error count", "errorcount", None, "mdi:counter", None],
}

DEVICE_STATUSSES = {
    0: "Not Connected",
    1: "Waiting",
    2: "Normal",
    3: "Error",
    4: "Upgrading",
}

FAULT_MESSAGES = {
    0: {
        0x80000000: "Code 81: Lost Communication D<->C",
        0x00080000: "Code 48: Master Fan4 Error",
        0x00040000: "Code 47: Master Fan3 Error",
        0x00020000: "Code 46: Master Fan2 Error",
        0x00010000: "Code 45: Master Fan1 Error",
        0x00002000: "Code 43: Master HW Phase3 Current High",
        0x00001000: "Code 42: Master HW Phase2 Current High",
        0x00000800: "Code 41: Master HW Phase1 Current High",
        0x00000400: "Code 40: Master HWPV2 Current High",
        0x00000200: "Code 39: Master HWPV1 Current High",
        0x00000100: "Code 38: Master HWBus Voltage High",
        0x00000010: "Code 37: Master Phase3 Current High",
        0x00000008: "Code 36: Master Phase2 Current High",
        0x00000004: "Code 35: Master Phase1 Current High",
        0x00000002: "Code 34: Master Bus Voltage Low",
        0x00000001: "Code 33: Master Bus Voltage High",
    },
    1: {
        0x80000000: "Code 32: Master Bus Voltage Balance Error",
        0x40000000: "Code 31: Master ISO Error",
        0x20000000: "Code 30: Master Phase3 DCI Error",
        0x10000000: "Code 29: Master Phase2 DCI Error",
        0x08000000: "Code 28: Master Phase1 DCI Error",
        0x04000000: "Code 27: Master GFCI Error",
        0x02000000: "Code 26: Master Phase3 No Grid Error",
        0x01000000: "Code 25: Master Phase2 No Grid Error",
        0x00800000: "Code 24: Master Phase1 No Grid Error",
        0x00400000: "Code 23: Master Phase3 Frequency Low",
        0x00200000: "Code 22: Master Phase3 Frequency High",
        0x00100000: "Code 21: Master Phase2 Frequency Low",
        0x00080000: "Code 20: Master Phase2 Frequency High",
        0x00040000: "Code 19: Master Phase1 Frequency Low",
        0x00020000: "Code 18: Master Phase1 Frequency High",
        0x00010000: "Code 17: Master Phase3 Voltage 10Min High",
        0x00008000: "Code 16: Master Phase2 Voltage 10Min High",
        0x00004000: "Code 15: Master Phase1 Voltage 10Min High",
        0x00002000: "Code 14: Master Phase3 Voltage Low",
        0x00001000: "Code 13: Master Phase3 Voltage High",
        0x00000800: "Code 12: Master Phase2 Voltage Low",
        0x00000400: "Code 11: Master Phase2 Voltage High",
        0x00000200: "Code 10: Master Phase1 Voltage Low",
        0x00000100: "Code 09: Master Phase1 Voltage High",
        0x00000080: "Code 08: Master Current Sensor Error",
        0x00000040: "Code 07: Master DCI Device Error",
        0x00000020: "Code 06: Master GFCI Device Error",
        0x00000010: "Code 05: Master Lost Communication M<->S",
        0x00000008: "Code 04: Master Temperature Low Error",
        0x00000004: "Code 03: Master Temperature High Error",
        0x00000002: "Code 02: Master EEPROM Error",
        0x00000001: "Code 01: Master Relay Error",
    },
    2: {
        0x40000000: "Code 80: Slave PV Voltage High Error",
        0x20000000: "Code 79: Slave PV2 Current High Error",
        0x10000000: "Code 78: Slave PV1 Current High Error",
        0x08000000: "Code 77: Slave PV2 Voltage High Error",
        0x04000000: "Code 76: Slave PV1 Voltage High Error",
        0x02000000: "Code 75: Slave Phase3 No Grid Error",
        0x01000000: "Code 74: Slave Phase2 No Grid Error",
        0x00800000: "Code 73: Slave Phase1 No Grid Error",
        0x00400000: "Code 72: Slave Phase3 Frequency Low",
        0x00200000: "Code 71: Slave Phase3 Frequency High",
        0x00100000: "Code 70: Slave Phase2 Frequency Low",
        0x00080000: "Code 69: Slave Phase2 Frequency High",
        0x00040000: "Code 68: Slave Phase1 Frequency Low",
        0x00020000: "Code 67: Slave Phase1 Frequency High",
        0x00010000: "Code 66: Slave Phase3 Voltage Low",
        0x00008000: "Code 65: Slave Phase3 Voltage High",
        0x00004000: "Code 64: Slave Phase2 Voltage Low",
        0x00002000: "Code 63: Slave Phase2 Voltage High",
        0x00001000: "Code 62: Slave Phase1 Voltage Low",
        0x00000800: "Code 61: Slave Phase1 Voltage High",
        0x00000400: "Code 60: Slave Phase3 DCI Consis Error",
        0x00000200: "Code 59: Slave Phase2 DCI Consis Error",
        0x00000100: "Code 58: Slave Phase1 DCI Consis Error",
        0x00000080: "Code 57: Slave GFCI Consis Error",
        0x00000040: "Code 56: Slave Phase3 Frequency Consis Error",
        0x00000020: "Code 55: Slave Phase2 Frequency Consis Error",
        0x00000010: "Code 54: Slave Phase1 Frequency Consis Error",
        0x00000008: "Code 53: Slave Phase3 Voltage Consis Error",
        0x00000004: "Code 52: Slave Phase2 Voltage Consis Error",
        0x00000002: "Code 51: Slave Phase1 Voltage Consis Error",
        0x00000001: "Code 50: Slave Lost Communication between M<->S",
    },
}
