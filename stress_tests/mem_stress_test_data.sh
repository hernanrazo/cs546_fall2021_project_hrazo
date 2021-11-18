#!/bin/bash

#sadf -d -- -u -r 2 5 | grep -v Average | grep -v Linux  >> stress_test.csv
sar -r -u 1 5 >> mem_stress_test_btrfs.txt
