# -*- coding: utf-8 -*-
from constants import *

# third party
from pyXSteam.XSteam import XSteam
steamTable = XSteam(XSteam.UNIT_SYSTEM_MKS)


INIT_DATA = {
    "PIk": 5, # степень повышения давления в компрессоре,
    "NtGTE": 6.3, # выходная мощность турбинны в ГТУ, МВт,
    "T1": 15 + KELVIN_CONST, # температура на входе в компрессор, К,
    "T4": 420 + KELVIN_CONST, # температура на выходе из турбинны, К,
    "p1": 0.1, # давление на входе в компрессор, МПа,
    "p6": 15, # давление на входе в паровую турбинну, МПа,
    "T6": 300 + KELVIN_CONST, # температура на входе в паровую турбинну, К,
    "T5": 150 + KELVIN_CONST, # температура газа на выходе из котла-утилизатора, К
    "Tcr": 17, # разница температур в конденсаторе
}
