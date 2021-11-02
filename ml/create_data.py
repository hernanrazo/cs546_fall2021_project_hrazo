import os
import sys
import random
import shutil
import h5py
import numpy as np
sys.path.append('../')
from utils.utils import create_dir

root_dir = str(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

# create txt files of varying size
def create_txt(counter: int) -> None:
    file_name = 'file' + str(counter) + '.txt'
    with open(file_name, 'wb') as f:
        num_bytes = random.randint(1, 10000)
        f.write(b"\0" * num_bytes)
    f.close()
    shutil.move(file_name, root_dir + '/data/txt/')


# create hdf5 file of varying size
def create_hd5(counter: int) -> None:
    file_name = 'file' + str(counter) + '.h5'
    d1 = np.random.random(size=(random.randint(1, 1000), random.randint(1, 1000)))
    h5 = h5py.File(file_name, 'w')
    h5.create_dataset('d1', data=d1)
    h5.close()
    shutil.move(file_name, root_dir + '/data/hdf5/')



def main():

    # create dirs for each file type
    create_dir(root_dir + '/data/txt/')
    create_dir(root_dir + '/data/hdf5/')

    # create 1000 of each file
    for i in range(1000):

        print('Creating random txt file ...')
        create_txt(i)

        print('Creating random h5 file ...')
        create_hd5(i)

if __name__ == '__main__':
    main()
