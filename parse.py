import sys
import re

signal_levels = {}

for line in sys.stdin.readlines():
    matches = re.findall(r'Quality=(\d+)', line)
    if matches:
        quality = int(matches[0])
    matches = re.findall(r'ESSID:"([^"]+)"', line)
    if matches:
        ssid = matches[0]
        signal_levels[ssid] = quality

keys = list(signal_levels.keys())
keys.sort()
for ssid in keys:
    level = signal_levels[ssid]
    print("%40s|%-70s|%2d" % (ssid, '=' * level, level))


