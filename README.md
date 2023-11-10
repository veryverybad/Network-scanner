# Requirements
```
pip3 install requests
pip3 install ipget
```
# Usage
```
>python3 scan.py
usage: yaru.py [-h] [--ip IP] [-i I] [-t T] [-n N] [-w] [-k] [-s]

指定したネットワーク内のIPアドレスとMACアドレス、ベンダー情報を表示します。(Displays IP and MAC addresses and
vendor information within the specified network)

options:
  -h, --help  show this help message and exit
  --ip IP     IPアドレスを入力(CIDR表記のマスク付き(/24,/23など))(Enter IP address (with
              mask in CIDR notation (/24,/23, etc.)))
  -i I        スキャンするインターフェイスを指定(Specify interface to scan)
  -t T        1ipあたりのスキャンする時間を指定する(-kや-
              sを使用してもこちらが優先させます)(デフォルトで0.2)(Specifies how long to scan per
              ip (this takes precedence over using -k or -s) (0.2 by
              default))
  -n N        1ipをスキャンする回数を指定(デフォルトで1)(Specifies the number of times to
              scan 1ip (default 1))
  -w          Windowsで使用可能にする(Make it available for Windows)
  -k          高速スキャンを使用する(精度は落ちる)(Use high-speed scanning (accuracy is
              reduced))
  -s          精密スキャンを使用する(時間はかかる)(Use precision scanning (takes time))
```
# Example of use
```
python3 scan.py
```
```
python3 scan.py -t 0.1 -n 1 -w
```
# Disclaimer
このソフトを犯罪目的で使用しても、作成者は一切の責任を負いません。(The author does not take any responsibility if this software is used for criminal purposes.)
