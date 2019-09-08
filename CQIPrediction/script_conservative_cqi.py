#!/usr/bin/python3

# Experiment setup
step = 10   # ms
experiment_time = 1000 # ms

import re

# read real CQI
fin = open("CQI_current", "r")
time_cqi = fin.read()
fin.close()

time_cqi_list = re.findall(r'\d+', time_cqi)
time_cqi_list = [int(i) for i in time_cqi_list]

time = 0
while time_cqi_list[time] < 400:
    time_cqi_list[time + 1] -= 3
    if  time_cqi_list[time + 1] < 0:
        time_cqi_list[time + 1] = 0
    time += 2

while time_cqi_list[time] < 1000:
    time_cqi_list[time + 1] -= 8
    if  time_cqi_list[time + 1] < 0:
        time_cqi_list[time + 1] = 0
    time += 2

i = 0
while i < 400:
    print(time_cqi_list[i], time_cqi_list[i + 1])
    i += 2;


