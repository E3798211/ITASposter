#!/usr/bin/python3

# Experiment setup
step = 10   # ms
experiment_time = 1000 # ms

import random

cur_time = 0
while cur_time < experiment_time / 4:
    cur_cqi = random.randint(2, 8)
    print("%d %d" % (cur_time, cur_cqi))
    cur_time += step
    print("%d %d" % (cur_time, cur_cqi))

while cur_time < experiment_time / 2:
    cur_cqi = random.randint(6, 12)
    print("%d %d" % (cur_time, cur_cqi))
    cur_time += step
    print("%d %d" % (cur_time, cur_cqi))

while cur_time < experiment_time * 3 / 4:
    cur_cqi = random.randint(9, 15)
    print("%d %d" % (cur_time, cur_cqi))
    cur_time += step
    print("%d %d" % (cur_time, cur_cqi))

while cur_time < experiment_time:
    cur_cqi = random.randint(9, 15)
    print("%d %d" % (cur_time, cur_cqi))
    cur_time += step
    print("%d %d" % (cur_time, cur_cqi))

