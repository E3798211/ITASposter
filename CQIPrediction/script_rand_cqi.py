#!/usr/bin/python3

# Experiment setup
step = 2   # ms
experiment_time = 50 # ms

import random

cur_time = 0
while cur_time < experiment_time:
    cur_cqi = random.randint(-13, 2)
    print("%d %d" % (cur_time, cur_cqi))
    cur_time += step;


