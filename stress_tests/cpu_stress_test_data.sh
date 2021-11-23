#!/bin/bash

# us sar to get cpu usage readings.
# Write results to a txt file (change filename as needed)
sar -u 1 60 >> /home/hernanrazo/project/stress_tests/cpu/userspace/cpu_zstd8.txt
