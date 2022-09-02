import sys
from pathlib import Path

# Add project path to system path to facilitate imports of the digital twin submodules
project_dir = Path(__file__).resolve().parents[1]
sys.path.append(str(project_dir) + "/submodules/python-pylontech")

import pylontech

bat1 = pylontech.Pylontech(serial_port="/home/mrx/bat1")

bat1.scan_for_batteries(16, 20)#scan address 16 to 20 the overall range is 0 to 255