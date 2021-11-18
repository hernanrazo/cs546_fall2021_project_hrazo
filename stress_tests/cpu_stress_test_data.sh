#!/bin/bash

# use sadf and sar to get cpu usage readings.
# 1000 readings every 1 second.
# Write results to cpu_stress_test.csv

#sadf -d -- -u 1 1000 | grep -v Average | grep -v Linux  >> cpu_stress_test.csv
sar -r -u 1 14 >> cpu_stress_test_btrfs.txt
