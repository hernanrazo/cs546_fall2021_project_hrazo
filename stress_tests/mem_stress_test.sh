#!/bin/bash

# compare disk performance with a simple 3:1 4K read/write test
# creates a 4 GB file and perform 4KB reads and writes using a 75%/25% split within the file, 
# with 64 operations running at a time.

fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=test --filename=test --bs=4k --iodepth=64 --size=4G --readwrite=randrw --rwmixread=75
