import sys
from pathlib import Path

# Add project path to system path to facilitate imports of the digital twin submodules
project_dir = Path(__file__).resolve().parents[1]
sys.path.append(str(project_dir) + "/submodules/python-pylontech")

import pylontech

bat1 = pylontech.Pylontech(serial_port="/home/mrx/bat1")
bat2 = pylontech.Pylontech(serial_port="/home/mrx/bat2")

bat1.scan_for_batteries(16, 20)

# print(bat2.get_module_serial_number(34))
# print(bat2.get_module_serial_number(35))
# print(bat2.get_module_serial_number(36))
# print(bat2.get_module_serial_number(37))
# print(bat2.get_module_serial_number(38))


# print(bat1.get_module_serial_number(18))
# print(bat1.get_module_serial_number(19))
# print(bat1.get_module_serial_number(20))
# print(bat1.get_module_serial_number(21))
# print(bat1.get_module_serial_number(22))