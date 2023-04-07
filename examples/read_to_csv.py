import pylontech
import subprocess, time, os, sys
from datetime import datetime



sys.path.append(os.getcwd() + '/..')
from csvWiter import csvWriter
from avg import avg

def parseCsvLine(data):
    r = [
        data["CycleNumber"],
        data["AverageBMSTemperature"],
        data["Current"],
        data["Power"],
        data["RemainingCapacity"],
        data["StateOfCharge"],
        data["TotalCapacity"],
        data["TotalPower"],
        data["Voltage"],
        data["GroupedCellsTemperatures"][0],
        data["GroupedCellsTemperatures"][1],
        data["GroupedCellsTemperatures"][2],
        data["GroupedCellsTemperatures"][3],
        data["CellVoltages"][0],
        data["CellVoltages"][1],
        data["CellVoltages"][2],
        data["CellVoltages"][3],
        data["CellVoltages"][4],
        data["CellVoltages"][5],
        data["CellVoltages"][6],
        data["CellVoltages"][7],
        data["CellVoltages"][8],
        data["CellVoltages"][9],
        data["CellVoltages"][10],
        data["CellVoltages"][11],
        data["CellVoltages"][12],
        data["CellVoltages"][13],
        data["CellVoltages"][14]
    ]

    return r

def genHeader():
    r = [
        "CycleNumber",
        "AverageBMSTemperature",
        "Current",
        "Power",
        "RemainingCapacity",
        "StateOfCharge",
        "TotalCapacity",
        "TotalPower",
        "Voltage",
        "GroupedCellsTemperatures0",
        "GroupedCellsTemperatures1",
        "GroupedCellsTemperatures2",
        "GroupedCellsTemperatures3",
        "CellVoltages0",
        "CellVoltages1",
        "CellVoltages2",
        "CellVoltages3",
        "CellVoltages4",
        "CellVoltages5",
        "CellVoltages6",
        "CellVoltages7",
        "CellVoltages8",
        "CellVoltages9",
        "CellVoltages10",
        "CellVoltages11",
        "CellVoltages12",
        "CellVoltages13",
        "CellVoltages14",
    ]

    return r


batList = {
    "bat1" : {
        "addr" : [18,19,20,21,22],
        "dev" : "/tmp/bat1",
        "ip" : "10.200.8.138",
        "port" : "26"
    },
    "bat2" : {
        "addr" : [34,35,36,37,38],
        "dev" : "/tmp/bat2",
        "ip" : "10.200.8.138",
        "port" : "32"
    }
}
batCSVList = {}
batHandle = {}
avgObj = {}

print("Create sockets")
for elm in batList:
    subprocess.Popen(["/usr/bin/socat", "pty,link=" + batList[elm]["dev"] + ",waitslave", "tcp:" + batList[elm]["ip"] + ":" + batList[elm]["port"]])
    time.sleep(1)# wait a second to create the socket
    batHandle.update({elm : pylontech.Pylontech(serial_port=batList[elm]["dev"])})

    #creat csv object per battery
    for addr in batList[elm]["addr"]:
        batCSVList.update({str(addr) : csvWriter("./data", "bat_" + str(addr), delimiter = ";", flushLines = 1)})
        header = genHeader()
        header.insert(0, "Count")
        header.insert(0, "Date")
        batCSVList[str(addr)].setHeader(header)
        avgObj.update({str(addr) : avg("minute")})
print("Start reading data")
while True:
    for elm in batList:
        for addr in batList[elm]["addr"]:
            data = parseCsvLine(batHandle[elm].get_values_single(addr))

            if avgObj[str(addr)].checkTime(datetime.now()):
                avgStarttime = avgObj[str(addr)].getStarttime()
                count = avgObj[str(addr)].getCount()
                lineData = avgObj[str(addr)].getData()
                lineData.insert(0, count)
                timeStr = f"{avgStarttime.strftime('%d/%m/%Y %H:%M:00')}"
                lineData.insert(0, timeStr)

                batCSVList[str(addr)].writeLine(lineData)

            avgObj[str(addr)].add(data)
