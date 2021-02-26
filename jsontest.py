#!/usr/bin/env python3
import json

with open("vms.json") as f:
    data = json.load(f)

for i in data['vm']:
    podid = i['pod']
    podip = i['ip']
    print(podid, podip)

connection = f"ssh {podip}"
print(connection)

