# Using
```
python3 zikken.py -h
usage: zikken.py [-h] [--scan SCAN] [--ip IP] [-w]

指定したネットワーク内のIPアドレスとMACアドレス、ベンダー情報を表示します(Displays IP and MAC addresses and
mac address vendor information within the specified network.)

options:
  -h, --help   show this help message and exit
  --scan SCAN  いくつのIPアドレスをスキャンするか？(How many IP addresses to scan?)
  --ip IP      IPアドレスの一番最後のピリオドまで入力(ピリオドは含む)(Enter the IP address up to the
               last period (periods are included))
  -w           Windowsで使用可能にする(Make it available for Windows)
```
## Example of use
```
python3 zikken.py --scan 250 --ip 192.168.1. -w
```
