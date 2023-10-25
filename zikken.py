import subprocess
import re
import requests
import datetime
import argparse
import threading

parser = argparse.ArgumentParser(description="指定したネットワーク内のIPアドレスとMACアドレス、ベンダー情報を表示します(Displays IP and MAC addresses and mac address vendor information within the specified network.)")
parser.add_argument("--scan",type=str,help="いくつのIPアドレスをスキャンするか？(How many IP addresses to scan?)")
parser.add_argument("--ip",type=str,help="IPアドレスの一番最後のピリオドまで入力(ピリオドは含む)(Enter the IP address up to the last period (periods are included))")
parser.add_argument('-w', action='store_true',help="Windowsで使用可能にする(Make it available for Windows)")
args = parser.parse_args()
nummber = args.scan
ipup = 0
getip = ""
shou = int(nummber) // 10
amari = int(nummber) % 10
inter = args.i
windows = args.w
if windows == True:
    sususu = "-n"
else:
    sususu = "-c"
def scaning1():
    global ipup
    global getip
    global shou
    global amari
    ipa = args.ip
    number = int(shou)*0
    scancan = int(shou)*1 + amari -1
    time1 = datetime.datetime.now()
    print(str(time1)+" "+"just" + "\n")
    ipaddress = str(ipa)+str(number)
    while number <= int(scancan):
        ipaddress = str(ipa)+str(number)
        scan =subprocess.run(["ping", sususu,"1","-W","100", ipaddress], stdout=subprocess.PIPE)
        if scan.returncode == 0:
            mac =subprocess.run(["arp","-a",ipaddress],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            match = re.search(r"([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})",str(mac))
            if match :
                macaddr = match.group()
                url = "https://api.macvendors.com/" + macaddr
                vendor = requests.get(url)
                vendor_name = vendor.text
                print(ipaddress)
                print(macaddr)
                if vendor_name =='{"errors":{"detail":"Not Found"}}':
                    print("Unknown" + "\n")
                else:
                    print(vendor_name + "\n")
                    getip += str(ipaddress) + " "
                    ipup += 1
                    number += 1
            else :
                number += 1
        else :
            mac =subprocess.run(["arp","-a",ipaddress],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            match = re.search(r"([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})",str(mac))
            if match :
                macaddr = match.group()
                url = "https://api.macvendors.com/" + macaddr
                vendor = requests.get(url)
                vendor_name = vendor.text
                print(ipaddress)
                print(macaddr)
                if vendor_name =='{"errors":{"detail":"Not Found"}}':
                    print("Unknown" + "\n")
                else:
                    print(vendor_name + "\n")
                    getip += str(ipaddress) + " "
                    ipup += 1
                    number += 1
            else :
                number += 1

def scaning2():
    global ipup
    global getip
    global shou
    global amari
    ipa = args.ip
    number = int(shou)*1
    scancan = int(shou)*2 - 1
    ipaddress = str(ipa)+str(number)
    while number <= int(scancan):
        ipaddress = str(ipa)+str(number)
        scan =subprocess.run(["ping", sususu,"1","-W","100", ipaddress], stdout=subprocess.PIPE)
        if scan.returncode == 0:
            mac =subprocess.run(["arp","-a",ipaddress],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            match = re.search(r"([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})",str(mac))
            if match :
                macaddr = match.group()
                url = "https://api.macvendors.com/" + macaddr
                vendor = requests.get(url)
                vendor_name = vendor.text
                print(ipaddress)
                print(macaddr)
                if vendor_name =='{"errors":{"detail":"Not Found"}}':
                    print("Unknown" + "\n")
                else:
                    print(vendor_name + "\n")
                getip += str(ipaddress) + " "
                ipup += 1
                number += 1
            else :
                number += 1
        else :
            mac =subprocess.run(["arp","-a",ipaddress],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            match = re.search(r"([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})",str(mac))
            if match :
                macaddr = match.group()
                url = "https://api.macvendors.com/" + macaddr
                vendor = requests.get(url)
                vendor_name = vendor.text
                print(ipaddress)
                print(macaddr)
                if vendor_name =='{"errors":{"detail":"Not Found"}}':
                    print("Unknown" + "\n")
                else:
                    print(vendor_name + "\n")
                    getip += str(ipaddress) + " "
                    ipup += 1
                    number += 1
            else :
                number += 1

def scaning3():
    global ipup
    global getip
    global shou
    global amari
    ipa = args.ip
    number = int(shou)*2
    scancan = int(shou)*3 - 1
    ipaddress = str(ipa)+str(number)
    while number <= int(scancan):
        ipaddress = str(ipa)+str(number)
        scan =subprocess.run(["ping", sususu,"1","-W","100", ipaddress], stdout=subprocess.PIPE)
        if scan.returncode == 0:
            mac =subprocess.run(["arp","-a",ipaddress],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            match = re.search(r"([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})",str(mac))
            if match :
                macaddr = match.group()
                url = "https://api.macvendors.com/" + macaddr
                vendor = requests.get(url)
                vendor_name = vendor.text
                print(ipaddress)
                print(macaddr)
                if vendor_name =='{"errors":{"detail":"Not Found"}}':
                    print("Unknown" + "\n")
                else:
                    print(vendor_name + "\n")
                getip += str(ipaddress) + " "
                ipup += 1
                number += 1
            else :
                number += 1
        else :
            mac =subprocess.run(["arp","-a",ipaddress],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            match = re.search(r"([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})",str(mac))
            if match :
                macaddr = match.group()
                url = "https://api.macvendors.com/" + macaddr
                vendor = requests.get(url)
                vendor_name = vendor.text
                print(ipaddress)
                print(macaddr)
                if vendor_name =='{"errors":{"detail":"Not Found"}}':
                    print("Unknown" + "\n")
                else:
                    print(vendor_name + "\n")
                    getip += str(ipaddress) + " "
                    ipup += 1
                    number += 1
            else :
                number += 1

def scaning4():
    global ipup
    global getip
    global shou
    global amari
    ipa = args.ip
    number = int(shou)*3
    scancan = int(shou)*4 - 1
    ipaddress = str(ipa)+str(number)
    while number <= int(scancan):
        ipaddress = str(ipa)+str(number)
        scan =subprocess.run(["ping", sususu,"1","-W","100", ipaddress], stdout=subprocess.PIPE)
        if scan.returncode == 0:
            mac =subprocess.run(["arp","-a",ipaddress],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            match = re.search(r"([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})",str(mac))
            if match :
                macaddr = match.group()
                url = "https://api.macvendors.com/" + macaddr
                vendor = requests.get(url)
                vendor_name = vendor.text
                print(ipaddress)
                print(macaddr)
                if vendor_name =='{"errors":{"detail":"Not Found"}}':
                    print("Unknown" + "\n")
                else:
                    print(vendor_name + "\n")
                getip += str(ipaddress) + " "
                ipup += 1
                number += 1
            else :
                number += 1
        else :
            mac =subprocess.run(["arp","-a",ipaddress],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            match = re.search(r"([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})",str(mac))
            if match :
                macaddr = match.group()
                url = "https://api.macvendors.com/" + macaddr
                vendor = requests.get(url)
                vendor_name = vendor.text
                print(ipaddress)
                print(macaddr)
                if vendor_name =='{"errors":{"detail":"Not Found"}}':
                    print("Unknown" + "\n")
                else:
                    print(vendor_name + "\n")
                    getip += str(ipaddress) + " "
                    ipup += 1
                    number += 1
            else :
                number += 1

def scaning5():
    global ipup
    global getip
    global shou
    global amari
    ipa = args.ip
    number = int(shou)*4
    scancan = int(shou)*5 - 1
    ipaddress = str(ipa)+str(number)
    while number <= int(scancan):
        ipaddress = str(ipa)+str(number)
        scan =subprocess.run(["ping", sususu,"1","-W","100", ipaddress], stdout=subprocess.PIPE)
        if scan.returncode == 0:
            mac =subprocess.run(["arp","-a",ipaddress],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            match = re.search(r"([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})",str(mac))
            if match :
                macaddr = match.group()
                url = "https://api.macvendors.com/" + macaddr
                vendor = requests.get(url)
                vendor_name = vendor.text
                print(ipaddress)
                print(macaddr)
                if vendor_name =='{"errors":{"detail":"Not Found"}}':
                    print("Unknown" + "\n")
                else:
                    print(vendor_name + "\n")
                getip += str(ipaddress) + " "
                ipup += 1
                number += 1
            else :
                number += 1
        else :
            mac =subprocess.run(["arp","-a",ipaddress],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            match = re.search(r"([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})",str(mac))
            if match :
                macaddr = match.group()
                url = "https://api.macvendors.com/" + macaddr
                vendor = requests.get(url)
                vendor_name = vendor.text
                print(ipaddress)
                print(macaddr)
                if vendor_name =='{"errors":{"detail":"Not Found"}}':
                    print("Unknown" + "\n")
                else:
                    print(vendor_name + "\n")
                    getip += str(ipaddress) + " "
                    ipup += 1
                    number += 1
            else :
                number += 1

def scaning6():
    global ipup
    global getip
    global shou
    global amari
    ipa = args.ip
    number = int(shou)*5
    scancan = int(shou)*6 - 1
    ipaddress = str(ipa)+str(number)
    while number <= int(scancan):
        ipaddress = str(ipa)+str(number)
        scan =subprocess.run(["ping", sususu,"1","-W","100", ipaddress], stdout=subprocess.PIPE)
        if scan.returncode == 0:
            mac =subprocess.run(["arp","-a",ipaddress],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            match = re.search(r"([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})",str(mac))
            if match :
                macaddr = match.group()
                url = "https://api.macvendors.com/" + macaddr
                vendor = requests.get(url)
                vendor_name = vendor.text
                print(ipaddress)
                print(macaddr)
                if vendor_name =='{"errors":{"detail":"Not Found"}}':
                    print("Unknown" + "\n")
                else:
                    print(vendor_name + "\n")
                getip += str(ipaddress) + " "
                ipup += 1
                number += 1
            else :
                number += 1
        else :
            mac =subprocess.run(["arp","-a",ipaddress],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            match = re.search(r"([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})",str(mac))
            if match :
                macaddr = match.group()
                url = "https://api.macvendors.com/" + macaddr
                vendor = requests.get(url)
                vendor_name = vendor.text
                print(ipaddress)
                print(macaddr)
                if vendor_name =='{"errors":{"detail":"Not Found"}}':
                    print("Unknown" + "\n")
                else:
                    print(vendor_name + "\n")
                    getip += str(ipaddress) + " "
                    ipup += 1
                    number += 1
            else :
                number += 1

def scaning7():
    global ipup
    global getip
    global shou
    global amari
    ipa = args.ip
    number = int(shou)*6
    scancan = int(shou)*7 - 1
    ipaddress = str(ipa)+str(number)
    while number <= int(scancan):
        ipaddress = str(ipa)+str(number)
        scan =subprocess.run(["ping", sususu,"1","-W","100", ipaddress], stdout=subprocess.PIPE)
        if scan.returncode == 0:
            mac =subprocess.run(["arp","-a",ipaddress],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            match = re.search(r"([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})",str(mac))
            if match :
                macaddr = match.group()
                url = "https://api.macvendors.com/" + macaddr
                vendor = requests.get(url)
                vendor_name = vendor.text
                print(ipaddress)
                print(macaddr)
                if vendor_name =='{"errors":{"detail":"Not Found"}}':
                    print("Unknown" + "\n")
                else:
                    print(vendor_name + "\n")
                getip += str(ipaddress) + " "
                ipup += 1
                number += 1
            else :
                number += 1
        else :
            mac =subprocess.run(["arp","-a",ipaddress],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            match = re.search(r"([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})",str(mac))
            if match :
                macaddr = match.group()
                url = "https://api.macvendors.com/" + macaddr
                vendor = requests.get(url)
                vendor_name = vendor.text
                print(ipaddress)
                print(macaddr)
                if vendor_name =='{"errors":{"detail":"Not Found"}}':
                    print("Unknown" + "\n")
                else:
                    print(vendor_name + "\n")
                    getip += str(ipaddress) + " "
                    ipup += 1
                    number += 1
            else :
                number += 1

def scaning8():
    global ipup
    global getip
    global shou
    global amari
    ipa = args.ip
    number = int(shou)*7
    scancan = int(shou)*8 - 1
    ipaddress = str(ipa)+str(number)
    while number <= int(scancan):
        ipaddress = str(ipa)+str(number)
        scan =subprocess.run(["ping", sususu,"1","-W","100", ipaddress], stdout=subprocess.PIPE)
        if scan.returncode == 0:
            mac =subprocess.run(["arp","-a",ipaddress],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            match = re.search(r"([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})",str(mac))
            if match :
                macaddr = match.group()
                url = "https://api.macvendors.com/" + macaddr
                vendor = requests.get(url)
                vendor_name = vendor.text
                print(ipaddress)
                print(macaddr)
                if vendor_name =='{"errors":{"detail":"Not Found"}}':
                    print("Unknown" + "\n")
                else:
                    print(vendor_name + "\n")
                getip += str(ipaddress) + " "
                ipup += 1
                number += 1
            else :
                number += 1
        else :
            mac =subprocess.run(["arp","-a",ipaddress],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            match = re.search(r"([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})",str(mac))
            if match :
                macaddr = match.group()
                url = "https://api.macvendors.com/" + macaddr
                vendor = requests.get(url)
                vendor_name = vendor.text
                print(ipaddress)
                print(macaddr)
                if vendor_name =='{"errors":{"detail":"Not Found"}}':
                    print("Unknown" + "\n")
                else:
                    print(vendor_name + "\n")
                    getip += str(ipaddress) + " "
                    ipup += 1
                    number += 1
            else :
                number += 1

def scaning9():
    global ipup
    global getip
    global shou
    global amari
    ipa = args.ip
    number = int(shou)*8
    scancan = int(shou)*9 - 1
    ipaddress = str(ipa)+str(number)
    while number <= int(scancan):
        ipaddress = str(ipa)+str(number)
        scan =subprocess.run(["ping", sususu,"1","-W","100", ipaddress], stdout=subprocess.PIPE)
        if scan.returncode == 0:
            mac =subprocess.run(["arp","-a",ipaddress],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            match = re.search(r"([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})",str(mac))
            if match :
                macaddr = match.group()
                url = "https://api.macvendors.com/" + macaddr
                vendor = requests.get(url)
                vendor_name = vendor.text
                print(ipaddress)
                print(macaddr)
                if vendor_name =='{"errors":{"detail":"Not Found"}}':
                    print("Unknown" + "\n")
                else:
                    print(vendor_name + "\n")
                getip += str(ipaddress) + " "
                ipup += 1
                number += 1
            else :
                number += 1
        else :
            mac =subprocess.run(["arp","-a",ipaddress],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            match = re.search(r"([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})",str(mac))
            if match :
                macaddr = match.group()
                url = "https://api.macvendors.com/" + macaddr
                vendor = requests.get(url)
                vendor_name = vendor.text
                print(ipaddress)
                print(macaddr)
                if vendor_name =='{"errors":{"detail":"Not Found"}}':
                    print("Unknown" + "\n")
                else:
                    print(vendor_name + "\n")
                    getip += str(ipaddress) + " "
                    ipup += 1
                    number += 1
            else :
                number += 1

def scaning10():
    global ipup
    global getip
    global shou
    global amari
    ipa = args.ip
    number = int(shou)*9
    scancan = int(shou)*10 - 1
    ipaddress = str(ipa)+str(number)
    while number <= int(scancan):
        ipaddress = str(ipa)+str(number)
        scan =subprocess.run(["ping", sususu,"1","-W","100", ipaddress], stdout=subprocess.PIPE)
        if scan.returncode == 0:
            mac =subprocess.run(["arp","-a",ipaddress],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            match = re.search(r"([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})",str(mac))
            if match :
                macaddr = match.group()
                url = "https://api.macvendors.com/" + macaddr
                vendor = requests.get(url)
                vendor_name = vendor.text
                print(ipaddress)
                print(macaddr)
                if vendor_name =='{"errors":{"detail":"Not Found"}}':
                    print("Unknown" + "\n")
                else:
                    print(vendor_name + "\n")
                getip += str(ipaddress) + " "
                ipup += 1
                number += 1
            else :
                number += 1
        else :
            mac =subprocess.run(["arp","-a",ipaddress],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            match = re.search(r"([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})",str(mac))
            if match :
                macaddr = match.group()
                url = "https://api.macvendors.com/" + macaddr
                vendor = requests.get(url)
                vendor_name = vendor.text
                print(ipaddress)
                print(macaddr)
                if vendor_name =='{"errors":{"detail":"Not Found"}}':
                    print("Unknown" + "\n")
                else:
                    print(vendor_name + "\n")
                    getip += str(ipaddress) + " "
                    ipup += 1
                    number += 1
            else :
                number += 1

maruti1 = threading.Thread(target=scaning1)
maruti2 = threading.Thread(target=scaning2)
maruti3 = threading.Thread(target=scaning3)
maruti4 = threading.Thread(target=scaning4)
maruti5 = threading.Thread(target=scaning5)
maruti6 = threading.Thread(target=scaning6)
maruti7 = threading.Thread(target=scaning7)
maruti8 = threading.Thread(target=scaning8)
maruti9 = threading.Thread(target=scaning9)
maruti10 = threading.Thread(target=scaning10)

maruti1.start()
maruti2.start()
maruti3.start()
maruti4.start()
maruti5.start()
maruti6.start()
maruti7.start()
maruti8.start()
maruti9.start()
maruti10.start()

maruti1.join()
maruti2.join()
maruti3.join()
maruti4.join()
maruti5.join()
maruti6.join()
maruti7.join()
maruti8.join()
maruti9.join()
maruti10.join()

print("\n" + str(ipup) + "host up" + "\n" + str(getip))