#!/bin/bash

# use sar to get the memory utilization readings.
# write results to a txt file (change the file name as needed)
sar -r 1 60 >> /home/hernanrazo/project/stress_tests/mem/userspace/mem_zstd8.txt
