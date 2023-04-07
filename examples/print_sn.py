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

for elm in batList:
    for addr in batList[elm]["addr"]:
        data = batHandle[elm].get_module_serial_number(addr)
        print(  "Bat " + str(addr) + "\t" +
                data["ModuleSerialNumber"].decode()
        )
