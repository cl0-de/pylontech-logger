import sys
from pathlib import Path

# # Add project path to system path to facilitate imports of the digital twin submodules
# project_dir = Path(__file__).resolve().parents[1]
# sys.path.append(str(project_dir) + "/submodules/python-pylontech")

import pylontech
import subprocess, time

batList = {
    "bat1" : {
        "addr" : [18,19,20,21,22],
        "dev" : "/home/mrx/bat1",
        "ip" : "10.200.8.138",
        "port" : "26"
    },
    "bat2" : {
        "addr" : [34,35,36,37,38],
        "dev" : "/home/mrx/bat2",
        "ip" : "10.200.8.138",
        "port" : "32"
    }
}

batHandle = {}
for elm in batList:
    subprocess.Popen(["/usr/bin/socat", "pty,link=" + batList[elm]["dev"] + ",waitslave", "tcp:" + batList[elm]["ip"] + ":" + batList[elm]["port"]])
    time.sleep(1)# wait a second to create the socket
    batHandle.update({elm : pylontech.Pylontech(serial_port=batList[elm]["dev"])})


while True:
    for elm in batList:
        for addr in batList[elm]["addr"]:
            data = batHandle[elm].get_values_single(addr)
            print(  "Bat " + str(addr) + "\t" +
                    str(data["CycleNumber"]/100) + "\t" +
                    str(data["Voltage"]) + "\t" +
                    str(data["TotalCapacity"]) + "\t" +
                    str(data["RemainingCapacity"]) + "\t"
            )
            #print(batHandle[elm].get_values_single(addr))
