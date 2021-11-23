#!/bin/bash

# use fio to test writing files. 
#test will write 25,600 MB file running 50 processes at a time

fio --name=randwrite --ioengine=libaio --iodepth=1 --rw=randwrite --bs=4k --direct=0 --size=512M --numjobs=50 --runtime=240 --group_reporting
