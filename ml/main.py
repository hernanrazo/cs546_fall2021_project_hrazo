import os
import pickle
import time
import numpy as np
import zlib
import lzo
import zstd
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


'''
Performance test for trained model. Measures the total times that each compression
library was used in general and for each file type. Also measures the average seconds
taken to compress using each library. Results are printed to a txt file.
'''

# constant bandwidth value.
# derived from measuring average time taken to write 1 GB to memory
BANDWIDTH = 1438.30 #MiB/s

root_dir = str(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

# get the write time
def get_write_time(time: float, file_size: float, ratio: float) -> float:
    return abs(time + file_size * ratio / BANDWIDTH)


# get avg of a list
def get_avg(list: list) -> float:
    return sum(list) / len(list)


# get the file type from the filename.
# map the file type to the corresponding int value used in training
# return int value
def get_file_type(filename: str) -> int:
    file_type = os.path.splitext(filename)[1]

    if file_type == '.txt':
        return 0
    elif file_type == '.jpg':
        return 1
    elif file_type == '.h5':
        return 2
    else: # pdf or PDF
        return 3


def main():
    
    # general counters
    none_counter = 0
    zlib_counter = 0
    lzo_counter = 0
    zstd_counter = 0

    # file type counters
    # count number of times a specific file type was used on a specific compression library
    txt_none = 0
    jpg_none = 0
    h5_none = 0
    pdf_none = 0
    
    txt_zlib = 0
    jpg_zlib = 0
    h5_zlib = 0
    pdf_zlib = 0
    
    txt_lzo = 0
    jpg_lzo = 0
    h5_lzo = 0
    pdf_lzo = 0
    
    txt_zstd = 0
    jpg_zstd = 0
    h5_zstd = 0
    pdf_zstd = 0
    
    # timer vars
    zlib_comp_timer = 0
    lzo_comp_timer = 0
    zstd_comp_timer = 0
    zlib_times = []
    lzo_times = []
    zstd_times = []


    # load trained model
    model = pickle.load(open(root_dir + '/saved_models/gbr-11-04-2021/gbr-python.sav', 'rb'))

    # iterate through all files
    for root, dirs, files in os.walk(root_dir + '/data/'):
        for file in files:
            print('Currently on: ' + os.path.join(root, file))

            # get size (in bytes) and file type of current file
            file_size = os.path.getsize(os.path.join(root, file))
            file_type = get_file_type(os.path.join(root, file))

            # use trained model to make inferences on what the compression time,
            # decompression time, and compression ratio will be for each library
            zlib_vals = np.asarray([file_type, file_size, 2]).reshape(1, -1)
            lzo_vals = np.asarray([file_type, file_size, 1]).reshape(1, -1)
            zstd_vals = np.asarray([file_type, file_size, 0]).reshape(1, -1)

            inf_zlib = model.predict(zlib_vals)
            inf_lzo = model.predict(lzo_vals)
            inf_zstd = model.predict(zstd_vals)

            # calculate resulting write times for all libraries and when no compression is used
            none = get_write_time(0, file_size, 1)
            zlib_time = get_write_time(inf_zlib[0][0], file_size, inf_zlib[0][2])
            lzo_time = get_write_time(inf_lzo[0][0], file_size, inf_lzo[0][2])
            zstd_time = get_write_time(inf_zstd[0][0], file_size, inf_zstd[0][2])

            # this is optimizing for fastest write time, so get the library that is fastest
            if none < zlib_time and none < lzo_time and none < zstd_time:
                fastest = 'none'
            elif zlib_time < none and zlib_time < lzo_time and zlib_time < zstd_time:
                fastest = 'zlib'
            elif lzo_time < none and lzo_time < zlib_time and lzo_time < zstd_time:
                fastest = 'lzo'
            elif zstd_time < none and zstd_time < lzo_time and zstd_time < zlib_time:
                fastest = 'zstd'

            # now actually compress using the fastest option
            #input = open(os.path.join(root, file), 'rb')
            with open(os.path.join(root, file), 'rb') as input:
                source_size = input.read()

            if fastest == 'none':
                print('No compression applied')
                none_counter += 1

                if file_type == 0:
                    txt_none += 1
                elif file_type == 1:
                    jpg_none += 1
                elif file_type == 2:
                    h5_none += 1
                else: # pdf or PDF
                    pdf_none += 1

            elif fastest == 'zlib':
                print('Compression using zlib')
                start = time.time()
                print(source_size)
                zlib.compress(source_size, 9)
                end = time.time()
                
                zlib_counter += 1
                timer = end - start
                zlib_times.append(timer)
                
                if file_type == 0:
                    txt_zlib += 1
                elif file_type == 1:
                    jpg_zlib += 1
                elif file_type == 2:
                    h5_zlib += 1
                else: # pdf or PDF
                    pdf_zlib += 1

            elif fastest == 'lzo':
                print('Compression using lzo')
                start = time.time()
                lzo.compress(source_size)
                end = time.time()
                
                lzo_counter += 1
                timer = end - start
                lzo_times.append(timer)
                
                if file_type == 0:
                    txt_lzo += 1
                elif file_type == 1:
                    jpg_lzo += 1
                elif file_type == 2:
                    h5_lzo += 1
                else: # pdf or PDF
                    pdf_lzo += 1

            elif fastest == 'zstd':
                print('Compression using zstd')
                start = time.time()
                zstd.compress(source_size, 1)
                end = time.time()
                
                zstd_counter += 1
                timer = end - start
                zstd_times.append(timer)
                
                if file_type == 0:
                    txt_zstd += 1
                elif file_type == 1:
                    jpg_zstd += 1
                elif file_type == 2:
                    h5_zstd += 1
                else: # pdf or PDF
                    pdf_zstd += 1

            input.close()
    

    # write final report
    print('\nPreparing report ...')
    f = open('report.txt', 'a')
    f.write('Performance results of trained model\n')
    f.write('\nTotal times no compression used: ' + str(none_counter))
    f.write('\nTotal times zlib used: ' +  str(zlib_counter))
    f.write('\nTotal times lzo used: ' + str(lzo_counter))
    f.write('\nTotal times zstd used: ' + str(zstd_counter))

    f.write('\n\nTotal times txt files used no compression: ' + str(txt_none))
    f.write('\nTotal times jpg files used no compression: ' + str(jpg_none))
    f.write('\nTotal times h5 files used no compression: ' + str(h5_none))
    f.write('\nTotal times pdf files used no compression: ' + str(pdf_none))

    f.write('\n\nTotal times txt files used zlib: ' + str(txt_zlib))
    f.write('\nTotal times jpg files used zlib: ' + str(jpg_zlib))
    f.write('\nTotal times h5 files used zlib: ' + str(h5_zlib))
    f.write('\nTotal times pdf files used zlib: ' + str(pdf_zlib))

    f.write('\n\nTotal times txt files used lzo: ' + str(txt_lzo))
    f.write('\nTotal times jpg files used lzo: ' + str(jpg_lzo))
    f.write('\nTotal times h5 files used lzo: ' + str(h5_lzo))
    f.write('\nTotal times pdf files used lzo: ' + str(pdf_lzo))
    
    f.write('\n\nTotal times txt files used zstd: ' + str(txt_zstd))
    f.write('\nTotal times jpg files used zstd: ' + str(jpg_zstd))
    f.write('\nTotal times h5 files used zstd: ' + str(h5_zstd))
    f.write('\nTotal times pdf files used zstd: ' + str(pdf_zstd))

    f.write('\n\nAvg time (seconds) to compress for zlib: ' + str('{:10f}'.format(get_avg(zlib_times))))
    f.write('\nAvg time (seconds) to compress for lzo: ' + str('{:10f}'.format(get_avg(lzo_times))))
    f.write('\nAvg time (seconds) to compress for zstd: ' + str('{:10f}\n'.format(get_avg(zstd_times))))
    f.close()
    print('done.')

if __name__ == '__main__':
    main()
