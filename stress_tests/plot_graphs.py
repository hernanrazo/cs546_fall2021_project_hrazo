import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
plot stress test data results into tables and
graphs using pandas and matplotlib
'''

root_dir = str(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

def main():

    # ====================================userspace graphs==============================

    # ==============================userspace memory usage data=========================

    # get data from txts for lzo
    mem_u_lzo1 = pd.read_csv(root_dir + '/stress_tests/mem/userspace/mem_lzo1.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_u_lzo2 = pd.read_csv(root_dir + '/stress_tests/mem/userspace/mem_lzo2.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_u_lzo4 = pd.read_csv(root_dir + '/stress_tests/mem/userspace/mem_lzo4.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_u_lzo8 = pd.read_csv(root_dir + '/stress_tests/mem/userspace/mem_lzo8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    mem_u_lzo1 = mem_u_lzo1.drop(mem_u_lzo1.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_u_lzo2 = mem_u_lzo2.drop(mem_u_lzo2.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_u_lzo4 = mem_u_lzo4.drop(mem_u_lzo4.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_u_lzo8 = mem_u_lzo8.drop(mem_u_lzo8.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)

    # remove last row (averages) 
    mem_u_lzo1.drop(mem_u_lzo1.tail(1).index, inplace=True)
    mem_u_lzo2.drop(mem_u_lzo2.tail(1).index, inplace=True)
    mem_u_lzo4.drop(mem_u_lzo4.tail(1).index, inplace=True)
    mem_u_lzo8.drop(mem_u_lzo8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    mem_lzo = pd.concat([mem_u_lzo1, mem_u_lzo2, mem_u_lzo4, mem_u_lzo8], axis=1)
    mem_lzo.index = np.arange(1, len(mem_lzo) + 1)
    mem_lzo.columns = ['1 process', '2 processes', '4 processes', '8 processes']
    
    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% Memory Used: LZO-Userspace')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% Memory Used')
    plt.legend()
    mem_lzo.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    mem_lzo.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    mem_lzo.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    mem_lzo.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/mem/lzo_userspace.png')
    plt.clf()
    del(mem_lzo)
    print('Done printing lzo_userspace.png')
    

    # get data from txts for zlib
    mem_u_zlib1 = pd.read_csv(root_dir + '/stress_tests/mem/userspace/mem_zlib1.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_u_zlib2 = pd.read_csv(root_dir + '/stress_tests/mem/userspace/mem_zlib2.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_u_zlib4 = pd.read_csv(root_dir + '/stress_tests/mem/userspace/mem_zlib4.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_u_zlib8 = pd.read_csv(root_dir + '/stress_tests/mem/userspace/mem_zlib8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    mem_u_zlib1 = mem_u_zlib1.drop(mem_u_zlib1.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_u_zlib2 = mem_u_zlib2.drop(mem_u_zlib2.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_u_zlib4 = mem_u_zlib4.drop(mem_u_zlib4.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_u_zlib8 = mem_u_zlib8.drop(mem_u_zlib8.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)

    # remove last row (averages) 
    mem_u_zlib1.drop(mem_u_zlib1.tail(1).index, inplace=True)
    mem_u_zlib2.drop(mem_u_zlib2.tail(1).index, inplace=True)
    mem_u_zlib4.drop(mem_u_zlib4.tail(1).index, inplace=True)
    mem_u_zlib8.drop(mem_u_zlib8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    mem_zlib = pd.concat([mem_u_zlib1, mem_u_zlib2, mem_u_zlib4, mem_u_zlib8], axis=1)
    mem_zlib.index = np.arange(1, len(mem_zlib) + 1)
    mem_zlib.columns = ['1 process', '2 processes', '4 processes', '8 processes']
    
    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% Memory Used: ZLIB-Userspace')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% Memory Used')
    plt.legend()
    mem_zlib.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    mem_zlib.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    mem_zlib.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    mem_zlib.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/mem/zlib_userspace.png')
    plt.clf()
    del(mem_zlib)
    print('Done printing zlib_userspace.png')


    # get data from txts for zstd
    mem_u_zstd1 = pd.read_csv(root_dir + '/stress_tests/mem/userspace/mem_zstd1.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_u_zstd2 = pd.read_csv(root_dir + '/stress_tests/mem/userspace/mem_zstd2.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_u_zstd4 = pd.read_csv(root_dir + '/stress_tests/mem/userspace/mem_zstd4.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_u_zstd8 = pd.read_csv(root_dir + '/stress_tests/mem/userspace/mem_zstd8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    mem_u_zstd1 = mem_u_zstd1.drop(mem_u_zstd1.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_u_zstd2 = mem_u_zstd2.drop(mem_u_zstd2.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_u_zstd4 = mem_u_zstd4.drop(mem_u_zstd4.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_u_zstd8 = mem_u_zstd8.drop(mem_u_zstd8.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)

    # remove last row (averages) 
    mem_u_zstd1.drop(mem_u_zstd1.tail(1).index, inplace=True)
    mem_u_zstd2.drop(mem_u_zstd2.tail(1).index, inplace=True)
    mem_u_zstd4.drop(mem_u_zstd4.tail(1).index, inplace=True)
    mem_u_zstd8.drop(mem_u_zstd8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    mem_zstd = pd.concat([mem_u_zstd1, mem_u_zstd2, mem_u_zstd4, mem_u_zstd8], axis=1)
    mem_zstd.index = np.arange(1, len(mem_zstd) + 1)
    mem_zstd.columns = ['1 process', '2 processes', '4 processes', '8 processes']
    
    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% Memory Used: ZSTD-Userspace')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% Memory Used')
    plt.legend()
    mem_zstd.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    mem_zstd.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    mem_zstd.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    mem_zstd.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/mem/zstd_userspace.png')
    plt.clf()
    del(mem_zstd)
    print('Done printing zstd_userspace.png')


    # get data from txts for no compression
    mem_u_none1 = pd.read_csv(root_dir + '/stress_tests/mem/userspace/mem_none1.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_u_none2 = pd.read_csv(root_dir + '/stress_tests/mem/userspace/mem_none2.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_u_none4 = pd.read_csv(root_dir + '/stress_tests/mem/userspace/mem_none4.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_u_none8 = pd.read_csv(root_dir + '/stress_tests/mem/userspace/mem_none8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    mem_u_none1 = mem_u_none1.drop(mem_u_none1.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_u_none2 = mem_u_none2.drop(mem_u_none2.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_u_none4 = mem_u_none4.drop(mem_u_none4.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_u_none8 = mem_u_none8.drop(mem_u_none8.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)

    # remove last row (averages) 
    mem_u_none1.drop(mem_u_none1.tail(1).index, inplace=True)
    mem_u_none2.drop(mem_u_none2.tail(1).index, inplace=True)
    mem_u_none4.drop(mem_u_none4.tail(1).index, inplace=True)
    mem_u_none8.drop(mem_u_none8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    mem_none = pd.concat([mem_u_none1, mem_u_none2, mem_u_none4, mem_u_none8], axis=1)
    mem_none.index = np.arange(1, len(mem_none) + 1)
    mem_none.columns = ['1 process', '2 processes', '4 processes', '8 processes']
    
    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% Memory Used: No Compression-Userspace')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% Memory Used')
    plt.legend()
    mem_none.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    mem_none.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    mem_none.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    mem_none.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/mem/none_userspace.png')
    plt.clf()
    del(mem_none)
    print('Done printing none_userspace.png')


    # ==========================userspace CPU (user mode) usage data====================
    # get data from txts for lzo 
    cpu_uu_lzo1 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_lzo1.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_uu_lzo2 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_lzo2.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_uu_lzo4 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_lzo4.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_uu_lzo8 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_lzo8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    cpu_uu_lzo1 = cpu_uu_lzo1.drop(cpu_uu_lzo1.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_uu_lzo2 = cpu_uu_lzo2.drop(cpu_uu_lzo2.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_uu_lzo4 = cpu_uu_lzo4.drop(cpu_uu_lzo4.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_uu_lzo8 = cpu_uu_lzo8.drop(cpu_uu_lzo8.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)

    # remove last row (averages) 
    cpu_uu_lzo1.drop(cpu_uu_lzo1.tail(1).index, inplace=True)
    cpu_uu_lzo2.drop(cpu_uu_lzo2.tail(1).index, inplace=True)
    cpu_uu_lzo4.drop(cpu_uu_lzo4.tail(1).index, inplace=True)
    cpu_uu_lzo8.drop(cpu_uu_lzo8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    cpu_lzo = pd.concat([cpu_uu_lzo1, cpu_uu_lzo2, cpu_uu_lzo4, cpu_uu_lzo8], axis=1)
    cpu_lzo.index = np.arange(1, len(cpu_lzo) + 1)
    cpu_lzo.columns = ['1 process', '2 processes', '4 processes', '8 processes']

    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% CPU Used (User Mode): LZO-Userspace')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% CPU Used (User Mode)')
    plt.legend()
    cpu_lzo.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    cpu_lzo.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    cpu_lzo.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    cpu_lzo.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/cpu/lzo_uu_userspace.png')
    plt.clf()
    del(cpu_lzo)
    print('Done printing lzo_uu_userspace.png')



    # get data from txts for zlib
    cpu_uu_zlib1 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_zlib1.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_uu_zlib2 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_zlib2.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_uu_zlib4 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_zlib4.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_uu_zlib8 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_zlib8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    cpu_uu_zlib1 = cpu_uu_zlib1.drop(cpu_uu_zlib1.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_uu_zlib2 = cpu_uu_zlib2.drop(cpu_uu_zlib2.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_uu_zlib4 = cpu_uu_zlib4.drop(cpu_uu_zlib4.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_uu_zlib8 = cpu_uu_zlib8.drop(cpu_uu_zlib8.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)

    # remove last row (averages) 
    cpu_uu_zlib1.drop(cpu_uu_zlib1.tail(1).index, inplace=True)
    cpu_uu_zlib2.drop(cpu_uu_zlib2.tail(1).index, inplace=True)
    cpu_uu_zlib4.drop(cpu_uu_zlib4.tail(1).index, inplace=True)
    cpu_uu_zlib8.drop(cpu_uu_zlib8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    cpu_zlib = pd.concat([cpu_uu_zlib1, cpu_uu_zlib2, cpu_uu_zlib4, cpu_uu_zlib8], axis=1)
    cpu_zlib.index = np.arange(1, len(cpu_zlib) + 1)
    cpu_zlib.columns = ['1 process', '2 processes', '4 processes', '8 processes']

    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% CPU Used (User Mode): ZLIB-Userspace')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% CPU Used (User Mode)')
    plt.legend()
    cpu_zlib.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    cpu_zlib.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    cpu_zlib.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    cpu_zlib.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/cpu/zlib_uu_userspace.png')
    plt.clf()
    del(cpu_zlib)
    print('Done printing zlib_uu_userspace.png')


    # get data from txts for zstd
    cpu_uu_zstd1 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_zstd1.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_uu_zstd2 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_zstd2.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_uu_zstd4 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_zstd4.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_uu_zstd8 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_zstd8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    cpu_uu_zstd1 = cpu_uu_zstd1.drop(cpu_uu_zstd1.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_uu_zstd2 = cpu_uu_zstd2.drop(cpu_uu_zstd2.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_uu_zstd4 = cpu_uu_zstd4.drop(cpu_uu_zstd4.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_uu_zstd8 = cpu_uu_zstd8.drop(cpu_uu_zstd8.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)

    # remove last row (averages) 
    cpu_uu_zstd1.drop(cpu_uu_zstd1.tail(1).index, inplace=True)
    cpu_uu_zstd2.drop(cpu_uu_zstd2.tail(1).index, inplace=True)
    cpu_uu_zstd4.drop(cpu_uu_zstd4.tail(1).index, inplace=True)
    cpu_uu_zstd8.drop(cpu_uu_zstd8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    cpu_zstd = pd.concat([cpu_uu_zstd1, cpu_uu_zstd2, cpu_uu_zstd4, cpu_uu_zstd8], axis=1)
    cpu_zstd.index = np.arange(1, len(cpu_zstd) + 1)
    cpu_zstd.columns = ['1 process', '2 processes', '4 processes', '8 processes']

    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% CPU Used (User Mode): ZSTD-Userspace')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% CPU Used (User Mode)')
    plt.legend()
    cpu_zstd.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    cpu_zstd.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    cpu_zstd.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    cpu_zstd.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/cpu/zstd_uu_userspace.png')
    plt.clf()
    del(cpu_zstd)
    print('Done printing zstd_uu_userspace.png')


    # get data from txts for no compression
    cpu_uu_none1 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_none1.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_uu_none2 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_none2.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_uu_none4 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_none4.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_uu_none8 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_none8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    cpu_uu_none1 = cpu_uu_none1.drop(cpu_uu_none1.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_uu_none2 = cpu_uu_none2.drop(cpu_uu_none2.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_uu_none4 = cpu_uu_none4.drop(cpu_uu_none4.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_uu_none8 = cpu_uu_none8.drop(cpu_uu_none8.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)

    # remove last row (averages) 
    cpu_uu_none1.drop(cpu_uu_none1.tail(1).index, inplace=True)
    cpu_uu_none2.drop(cpu_uu_none2.tail(1).index, inplace=True)
    cpu_uu_none4.drop(cpu_uu_none4.tail(1).index, inplace=True)
    cpu_uu_none8.drop(cpu_uu_none8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    cpu_none = pd.concat([cpu_uu_none1, cpu_uu_none2, cpu_uu_none4, cpu_uu_none8], axis=1)
    cpu_none.index = np.arange(1, len(cpu_none) + 1)
    cpu_none.columns = ['1 process', '2 processes', '4 processes', '8 processes']

    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% CPU Used (User Mode): No Compression-Userspace')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% CPU Used (User Mode)')
    plt.legend()
    cpu_none.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    cpu_none.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    cpu_none.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    cpu_none.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/cpu/none_uu_userspace.png')
    plt.clf()
    del(cpu_none)
    print('Done printing none_uu_userspace.png')
    


    # ==========================userspace CPU (system mode) usage data==================

    # get data from txts for lzo
    cpu_us_lzo1 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_lzo1.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_us_lzo2 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_lzo2.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_us_lzo4 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_lzo4.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_us_lzo8 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_lzo8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    cpu_us_lzo1 = cpu_us_lzo1.drop(cpu_us_lzo1.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_us_lzo2 = cpu_us_lzo2.drop(cpu_us_lzo2.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_us_lzo4 = cpu_us_lzo4.drop(cpu_us_lzo4.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_us_lzo8 = cpu_us_lzo8.drop(cpu_us_lzo8.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)

    # remove last row (averages) 
    cpu_us_lzo1.drop(cpu_us_lzo1.tail(1).index, inplace=True)
    cpu_us_lzo2.drop(cpu_us_lzo2.tail(1).index, inplace=True)
    cpu_us_lzo4.drop(cpu_us_lzo4.tail(1).index, inplace=True)
    cpu_us_lzo8.drop(cpu_us_lzo8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    cpu_lzo = pd.concat([cpu_us_lzo1, cpu_us_lzo2, cpu_us_lzo4, cpu_us_lzo8], axis=1)
    cpu_lzo.index = np.arange(1, len(cpu_lzo) + 1)
    cpu_lzo.columns = ['1 process', '2 processes', '4 processes', '8 processes']

    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% CPU Used (System Mode): LZO-Userspace')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% CPU Used (System Mode)')
    plt.legend()
    cpu_lzo.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    cpu_lzo.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    cpu_lzo.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    cpu_lzo.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/cpu/lzo_us_userspace.png')
    plt.clf()
    del(cpu_lzo)
    print('Done printing lzo_us_userspace.png')



    # get data from txts for zlib 
    cpu_us_zlib1 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_zlib1.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_us_zlib2 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_zlib2.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_us_zlib4 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_zlib4.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_us_zlib8 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_zlib8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    cpu_us_zlib1 = cpu_us_zlib1.drop(cpu_us_zlib1.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_us_zlib2 = cpu_us_zlib2.drop(cpu_us_zlib2.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_us_zlib4 = cpu_us_zlib4.drop(cpu_us_zlib4.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_us_zlib8 = cpu_us_zlib8.drop(cpu_us_zlib8.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)

    # remove last row (averages) 
    cpu_us_zlib1.drop(cpu_us_zlib1.tail(1).index, inplace=True)
    cpu_us_zlib2.drop(cpu_us_zlib2.tail(1).index, inplace=True)
    cpu_us_zlib4.drop(cpu_us_zlib4.tail(1).index, inplace=True)
    cpu_us_zlib8.drop(cpu_us_zlib8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    cpu_zlib = pd.concat([cpu_us_zlib1, cpu_us_zlib2, cpu_us_zlib4, cpu_us_zlib8], axis=1)
    cpu_zlib.index = np.arange(1, len(cpu_zlib) + 1)
    cpu_zlib.columns = ['1 process', '2 processes', '4 processes', '8 processes']

    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% CPU Used (System Mode): ZLIB-Userspace')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% CPU Used (System Mode)')
    plt.legend()
    cpu_zlib.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    cpu_zlib.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    cpu_zlib.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    cpu_zlib.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/cpu/zlib_us_userspace.png')
    plt.clf()
    del(cpu_zlib)
    print('Done printing zlib_us_userspace.png')


    # get data from txts for zstd
    cpu_us_zstd1 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_zstd1.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_us_zstd2 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_zstd2.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_us_zstd4 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_zstd4.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_us_zstd8 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_zstd8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    cpu_us_zstd1 = cpu_us_zstd1.drop(cpu_us_zstd1.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_us_zstd2 = cpu_us_zstd2.drop(cpu_us_zstd2.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_us_zstd4 = cpu_us_zstd4.drop(cpu_us_zstd4.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_us_zstd8 = cpu_us_zstd8.drop(cpu_us_zstd8.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)

    # remove last row (averages) 
    cpu_us_zstd1.drop(cpu_us_zstd1.tail(1).index, inplace=True)
    cpu_us_zstd2.drop(cpu_us_zstd2.tail(1).index, inplace=True)
    cpu_us_zstd4.drop(cpu_us_zstd4.tail(1).index, inplace=True)
    cpu_us_zstd8.drop(cpu_us_zstd8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    cpu_zstd = pd.concat([cpu_us_zstd1, cpu_us_zstd2, cpu_us_zstd4, cpu_us_zstd8], axis=1)
    cpu_zstd.index = np.arange(1, len(cpu_zstd) + 1)
    cpu_zstd.columns = ['1 process', '2 processes', '4 processes', '8 processes']

    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% CPU Used (System Mode): ZSTD-Userspace')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% CPU Used (System Mode)')
    plt.legend()
    cpu_zstd.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    cpu_zstd.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    cpu_zstd.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    cpu_zstd.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/cpu/zstd_us_userspace.png')
    plt.clf()
    del(cpu_zstd)
    print('Done printing zstd_us_userspace.png')


    # get data from txts for no compression
    cpu_us_none1 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_none1.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_us_none2 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_none2.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_us_none4 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_none4.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_us_none8 = pd.read_csv(root_dir + '/stress_tests/cpu/userspace/cpu_none8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    cpu_us_none1 = cpu_us_none1.drop(cpu_us_none1.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_us_none2 = cpu_us_none2.drop(cpu_us_none2.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_us_none4 = cpu_us_none4.drop(cpu_us_none4.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_us_none8 = cpu_us_none8.drop(cpu_us_none8.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)

    # remove last row (averages) 
    cpu_us_none1.drop(cpu_us_none1.tail(1).index, inplace=True)
    cpu_us_none2.drop(cpu_us_none2.tail(1).index, inplace=True)
    cpu_us_none4.drop(cpu_us_none4.tail(1).index, inplace=True)
    cpu_us_none8.drop(cpu_us_none8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    cpu_none = pd.concat([cpu_us_lzo1, cpu_us_lzo2, cpu_us_lzo4, cpu_us_lzo8], axis=1)
    cpu_none.index = np.arange(1, len(cpu_none) + 1)
    cpu_none.columns = ['1 process', '2 processes', '4 processes', '8 processes']

    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% CPU Used (System Mode): No Compression-Userspace')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% CPU Used (System Mode)')
    plt.legend()
    cpu_none.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    cpu_none.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    cpu_none.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    cpu_none.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/cpu/none_us_userspace.png')
    plt.clf()
    del(cpu_none)
    print('Done printing none_us_userspace.png')



    # ======================================BTRFS graphs================================

    # ================================BTFS memory usage data============================
    mem_b_lzo1 = pd.read_csv(root_dir + '/stress_tests/mem/btrfs/mem_lzo1.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_b_lzo2 = pd.read_csv(root_dir + '/stress_tests/mem/btrfs/mem_lzo2.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_b_lzo4 = pd.read_csv(root_dir + '/stress_tests/mem/btrfs/mem_lzo4.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_b_lzo8 = pd.read_csv(root_dir + '/stress_tests/mem/btrfs/mem_lzo8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    mem_b_lzo1 = mem_b_lzo1.drop(mem_b_lzo1.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_b_lzo2 = mem_b_lzo2.drop(mem_b_lzo2.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_b_lzo4 = mem_b_lzo4.drop(mem_b_lzo4.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_b_lzo8 = mem_b_lzo8.drop(mem_b_lzo8.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)

    # remove last row (averages) 
    mem_b_lzo1.drop(mem_b_lzo1.tail(1).index, inplace=True)
    mem_b_lzo2.drop(mem_b_lzo2.tail(1).index, inplace=True)
    mem_b_lzo4.drop(mem_b_lzo4.tail(1).index, inplace=True)
    mem_b_lzo8.drop(mem_b_lzo8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    mem_lzo = pd.concat([mem_b_lzo1, mem_b_lzo2, mem_b_lzo4, mem_b_lzo8], axis=1)
    mem_lzo.index = np.arange(1, len(mem_lzo) + 1)
    mem_lzo.columns = ['1 process', '2 processes', '4 processes', '8 processes']
    
    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% Memory Used: LZO-btrfs')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% Memory Used')
    plt.legend()
    mem_lzo.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    mem_lzo.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    mem_lzo.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    mem_lzo.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/mem/lzo_btrfs.png')
    plt.clf()
    del(mem_lzo)
    print('Done printing lzo_btrfs.png')
    

    # get data from txts for zlib
    mem_b_zlib1 = pd.read_csv(root_dir + '/stress_tests/mem/btrfs/mem_zlib1.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_b_zlib2 = pd.read_csv(root_dir + '/stress_tests/mem/btrfs/mem_zlib2.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_b_zlib4 = pd.read_csv(root_dir + '/stress_tests/mem/btrfs/mem_zlib4.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_b_zlib8 = pd.read_csv(root_dir + '/stress_tests/mem/btrfs/mem_zlib8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    mem_b_zlib1 = mem_b_zlib1.drop(mem_b_zlib1.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_b_zlib2 = mem_b_zlib2.drop(mem_b_zlib2.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_b_zlib4 = mem_b_zlib4.drop(mem_b_zlib4.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_b_zlib8 = mem_b_zlib8.drop(mem_b_zlib8.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)

    # remove last row (averages) 
    mem_b_zlib1.drop(mem_b_zlib1.tail(1).index, inplace=True)
    mem_b_zlib2.drop(mem_b_zlib2.tail(1).index, inplace=True)
    mem_b_zlib4.drop(mem_b_zlib4.tail(1).index, inplace=True)
    mem_b_zlib8.drop(mem_b_zlib8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    mem_zlib = pd.concat([mem_b_zlib1, mem_b_zlib2, mem_b_zlib4, mem_b_zlib8], axis=1)
    mem_zlib.index = np.arange(1, len(mem_zlib) + 1)
    mem_zlib.columns = ['1 process', '2 processes', '4 processes', '8 processes']
    
    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% Memory Used: ZLIB-btrfs')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% Memory Used')
    plt.legend()
    mem_zlib.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    mem_zlib.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    mem_zlib.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    mem_zlib.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/mem/zlib_btrfs.png')
    plt.clf()
    del(mem_zlib)
    print('Done printing zlib_btrfs.png')


    # get data from txts for zstd
    mem_b_zstd1 = pd.read_csv(root_dir + '/stress_tests/mem/btrfs/mem_zstd1.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_b_zstd2 = pd.read_csv(root_dir + '/stress_tests/mem/btrfs/mem_zstd2.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_b_zstd4 = pd.read_csv(root_dir + '/stress_tests/mem/btrfs/mem_zstd4.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_b_zstd8 = pd.read_csv(root_dir + '/stress_tests/mem/btrfs/mem_zstd8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    mem_b_zstd1 = mem_b_zstd1.drop(mem_b_zstd1.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_b_zstd2 = mem_b_zstd2.drop(mem_b_zstd2.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_b_zstd4 = mem_b_zstd4.drop(mem_b_zstd4.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_b_zstd8 = mem_b_zstd8.drop(mem_b_zstd8.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)

    # remove last row (averages) 
    mem_b_zstd1.drop(mem_b_zstd1.tail(1).index, inplace=True)
    mem_b_zstd2.drop(mem_b_zstd2.tail(1).index, inplace=True)
    mem_b_zstd4.drop(mem_b_zstd4.tail(1).index, inplace=True)
    mem_b_zstd8.drop(mem_b_zstd8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    mem_zstd = pd.concat([mem_b_zstd1, mem_b_zstd2, mem_b_zstd4, mem_b_zstd8], axis=1)
    mem_zstd.index = np.arange(1, len(mem_zstd) + 1)
    mem_zstd.columns = ['1 process', '2 processes', '4 processes', '8 processes']
    
    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% Memory Used: ZSTD-Userspace')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% Memory Used')
    plt.legend()
    mem_zstd.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    mem_zstd.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    mem_zstd.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    mem_zstd.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/mem/zstd_btrfs.png')
    plt.clf()
    del(mem_zstd)
    print('Done printing zstd_btrfs.png')


    # get data from txts for no compression
    mem_b_none1 = pd.read_csv(root_dir + '/stress_tests/mem/btrfs/mem_none1.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_b_none2 = pd.read_csv(root_dir + '/stress_tests/mem/btrfs/mem_none2.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_b_none4 = pd.read_csv(root_dir + '/stress_tests/mem/btrfs/mem_none4.txt', skiprows=3, delim_whitespace=True, header=None)
    mem_b_none8 = pd.read_csv(root_dir + '/stress_tests/mem/btrfs/mem_none8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    mem_b_none1 = mem_b_none1.drop(mem_b_none1.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_b_none2 = mem_b_none2.drop(mem_b_none2.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_b_none4 = mem_b_none4.drop(mem_b_none4.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)
    mem_b_none8 = mem_b_none8.drop(mem_b_none8.columns[[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]], axis=1)

    # remove last row (averages) 
    mem_b_none1.drop(mem_b_none1.tail(1).index, inplace=True)
    mem_b_none2.drop(mem_b_none2.tail(1).index, inplace=True)
    mem_b_none4.drop(mem_b_none4.tail(1).index, inplace=True)
    mem_b_none8.drop(mem_b_none8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    mem_none = pd.concat([mem_b_none1, mem_b_none2, mem_b_none4, mem_b_none8], axis=1)
    mem_none.index = np.arange(1, len(mem_none) + 1)
    mem_none.columns = ['1 process', '2 processes', '4 processes', '8 processes']
    
    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% Memory Used: No Compression-btrfs')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% Memory Used')
    plt.legend()
    mem_none.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    mem_none.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    mem_none.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    mem_none.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/mem/none_btrfs.png')
    plt.clf()
    del(mem_none)
    print('Done printing none_btrfs.png')


    # ==========================BTRFS CPU (user mode) usage data========================
    # get data from txts for lzo 
    cpu_bu_lzo1 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_lzo1.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bu_lzo2 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_lzo2.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bu_lzo4 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_lzo4.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bu_lzo8 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_lzo8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    cpu_bu_lzo1 = cpu_bu_lzo1.drop(cpu_bu_lzo1.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_bu_lzo2 = cpu_bu_lzo2.drop(cpu_bu_lzo2.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_bu_lzo4 = cpu_bu_lzo4.drop(cpu_bu_lzo4.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_bu_lzo8 = cpu_bu_lzo8.drop(cpu_bu_lzo8.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)

    # remove last row (averages) 
    cpu_bu_lzo1.drop(cpu_bu_lzo1.tail(1).index, inplace=True)
    cpu_bu_lzo2.drop(cpu_bu_lzo2.tail(1).index, inplace=True)
    cpu_bu_lzo4.drop(cpu_bu_lzo4.tail(1).index, inplace=True)
    cpu_bu_lzo8.drop(cpu_bu_lzo8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    cpu_lzo = pd.concat([cpu_bu_lzo1, cpu_bu_lzo2, cpu_bu_lzo4, cpu_bu_lzo8], axis=1)
    cpu_lzo.index = np.arange(1, len(cpu_lzo) + 1)
    cpu_lzo.columns = ['1 process', '2 processes', '4 processes', '8 processes']

    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% CPU Used (User Mode): LZO-btrfs')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% CPU Used (User Mode)')
    plt.legend()
    cpu_lzo.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    cpu_lzo.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    cpu_lzo.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    cpu_lzo.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/cpu/lzo_bu_btrfs.png')
    plt.clf()
    del(cpu_lzo)
    print('Done printing lzo_bu_btrfs.png')



    # get data from txts for zlib
    cpu_bu_zlib1 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_zlib1.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bu_zlib2 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_zlib2.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bu_zlib4 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_zlib4.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bu_zlib8 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_zlib8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    cpu_bu_zlib1 = cpu_bu_zlib1.drop(cpu_bu_zlib1.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_bu_zlib2 = cpu_bu_zlib2.drop(cpu_bu_zlib2.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_bu_zlib4 = cpu_bu_zlib4.drop(cpu_bu_zlib4.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_bu_zlib8 = cpu_bu_zlib8.drop(cpu_bu_zlib8.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)

    # remove last row (averages) 
    cpu_bu_zlib1.drop(cpu_bu_zlib1.tail(1).index, inplace=True)
    cpu_bu_zlib2.drop(cpu_bu_zlib2.tail(1).index, inplace=True)
    cpu_bu_zlib4.drop(cpu_bu_zlib4.tail(1).index, inplace=True)
    cpu_bu_zlib8.drop(cpu_bu_zlib8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    cpu_zlib = pd.concat([cpu_bu_zlib1, cpu_bu_zlib2, cpu_bu_zlib4, cpu_bu_zlib8], axis=1)
    cpu_zlib.index = np.arange(1, len(cpu_zlib) + 1)
    cpu_zlib.columns = ['1 process', '2 processes', '4 processes', '8 processes']

    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% CPU Used (User Mode): ZLIB-btrfs')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% CPU Used (User Mode)')
    plt.legend()
    cpu_zlib.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    cpu_zlib.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    cpu_zlib.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    cpu_zlib.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/cpu/zlib_bu_btrfs.png')
    plt.clf()
    del(cpu_zlib)
    print('Done printing zlib_bu_btrfs.png')


    # get data from txts for zstd
    cpu_bu_zstd1 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_zstd1.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bu_zstd2 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_zstd2.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bu_zstd4 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_zstd4.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bu_zstd8 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_zstd8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    cpu_bu_zstd1 = cpu_bu_zstd1.drop(cpu_bu_zstd1.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_bu_zstd2 = cpu_bu_zstd2.drop(cpu_bu_zstd2.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_bu_zstd4 = cpu_bu_zstd4.drop(cpu_bu_zstd4.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_bu_zstd8 = cpu_bu_zstd8.drop(cpu_bu_zstd8.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)

    # remove last row (averages) 
    cpu_bu_zstd1.drop(cpu_bu_zstd1.tail(1).index, inplace=True)
    cpu_bu_zstd2.drop(cpu_bu_zstd2.tail(1).index, inplace=True)
    cpu_bu_zstd4.drop(cpu_bu_zstd4.tail(1).index, inplace=True)
    cpu_bu_zstd8.drop(cpu_bu_zstd8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    cpu_zstd = pd.concat([cpu_bu_zstd1, cpu_bu_zstd2, cpu_bu_zstd4, cpu_bu_zstd8], axis=1)
    cpu_zstd.index = np.arange(1, len(cpu_zstd) + 1)
    cpu_zstd.columns = ['1 process', '2 processes', '4 processes', '8 processes']

    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% CPU Used (User Mode): ZSTD-btrfs')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% CPU Used (User Mode)')
    plt.legend()
    cpu_zstd.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    cpu_zstd.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    cpu_zstd.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    cpu_zstd.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/cpu/zstd_bu_btrfs.png')
    plt.clf()
    del(cpu_zstd)
    print('Done printing zstd_bu_btrfs.png')


    # get data from txts for no compression
    cpu_bu_none1 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_none1.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bu_none2 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_none2.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bu_none4 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_none4.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bu_none8 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_none8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    cpu_bu_none1 = cpu_bu_none1.drop(cpu_bu_none1.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_bu_none2 = cpu_bu_none2.drop(cpu_bu_none2.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_bu_none4 = cpu_bu_none4.drop(cpu_bu_none4.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)
    cpu_bu_none8 = cpu_bu_none8.drop(cpu_bu_none8.columns[[0, 1, 2, 4, 5, 6, 7, 8]], axis=1)

    # remove last row (averages) 
    cpu_bu_none1.drop(cpu_bu_none1.tail(1).index, inplace=True)
    cpu_bu_none2.drop(cpu_bu_none2.tail(1).index, inplace=True)
    cpu_bu_none4.drop(cpu_bu_none4.tail(1).index, inplace=True)
    cpu_bu_none8.drop(cpu_bu_none8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    cpu_none = pd.concat([cpu_bu_none1, cpu_bu_none2, cpu_bu_none4, cpu_bu_none8], axis=1)
    cpu_none.index = np.arange(1, len(cpu_none) + 1)
    cpu_none.columns = ['1 process', '2 processes', '4 processes', '8 processes']

    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% CPU Used (User Mode): No Compression-btrfs')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% CPU Used (User Mode)')
    plt.legend()
    cpu_none.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    cpu_none.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    cpu_none.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    cpu_none.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/cpu/none_bu_btrfs.png')
    plt.clf()
    del(cpu_none)
    print('Done printing none_bu_btrfs.png')
    


    # ==========================BTRFS CPU (system mode) usage data=======================

    # get data from txts for lzo
    cpu_bs_lzo1 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_lzo1.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bs_lzo2 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_lzo2.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bs_lzo4 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_lzo4.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bs_lzo8 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_lzo8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    cpu_bs_lzo1 = cpu_bs_lzo1.drop(cpu_bs_lzo1.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_bs_lzo2 = cpu_bs_lzo2.drop(cpu_bs_lzo2.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_bs_lzo4 = cpu_bs_lzo4.drop(cpu_bs_lzo4.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_bs_lzo8 = cpu_bs_lzo8.drop(cpu_bs_lzo8.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)

    # remove last row (averages) 
    cpu_bs_lzo1.drop(cpu_bs_lzo1.tail(1).index, inplace=True)
    cpu_bs_lzo2.drop(cpu_bs_lzo2.tail(1).index, inplace=True)
    cpu_bs_lzo4.drop(cpu_bs_lzo4.tail(1).index, inplace=True)
    cpu_bs_lzo8.drop(cpu_bs_lzo8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    cpu_lzo = pd.concat([cpu_bs_lzo1, cpu_bs_lzo2, cpu_bs_lzo4, cpu_bs_lzo8], axis=1)
    cpu_lzo.index = np.arange(1, len(cpu_lzo) + 1)
    cpu_lzo.columns = ['1 process', '2 processes', '4 processes', '8 processes']

    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% CPU Used (System Mode): LZO-btrfs')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% CPU Used (System Mode)')
    plt.legend()
    cpu_lzo.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    cpu_lzo.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    cpu_lzo.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    cpu_lzo.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/cpu/lzo_bs_btrfs.png')
    plt.clf()
    del(cpu_lzo)
    print('Done printing lzo_bs_btrfs.png')



    # get data from txts for zlib 
    cpu_bs_zlib1 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_zlib1.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bs_zlib2 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_zlib2.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bs_zlib4 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_zlib4.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bs_zlib8 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_zlib8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    cpu_bs_zlib1 = cpu_bs_zlib1.drop(cpu_bs_zlib1.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_bs_zlib2 = cpu_bs_zlib2.drop(cpu_bs_zlib2.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_bs_zlib4 = cpu_bs_zlib4.drop(cpu_bs_zlib4.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_bs_zlib8 = cpu_bs_zlib8.drop(cpu_bs_zlib8.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)

    # remove last row (averages) 
    cpu_bs_zlib1.drop(cpu_us_zlib1.tail(1).index, inplace=True)
    cpu_bs_zlib2.drop(cpu_bs_zlib2.tail(1).index, inplace=True)
    cpu_bs_zlib4.drop(cpu_bs_zlib4.tail(1).index, inplace=True)
    cpu_bs_zlib8.drop(cpu_bs_zlib8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    cpu_zlib = pd.concat([cpu_bs_zlib1, cpu_bs_zlib2, cpu_bs_zlib4, cpu_bs_zlib8], axis=1)
    cpu_zlib.index = np.arange(1, len(cpu_zlib) + 1)
    cpu_zlib.columns = ['1 process', '2 processes', '4 processes', '8 processes']

    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% CPU Used (System Mode): ZLIB-btrfs')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% CPU Used (System Mode)')
    plt.legend()
    cpu_zlib.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    cpu_zlib.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    cpu_zlib.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    cpu_zlib.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/cpu/zlib_bs_btrfs.png')
    plt.clf()
    del(cpu_zlib)
    print('Done printing zlib_bs_btrfs.png')


    # get data from txts for zstd
    cpu_bs_zstd1 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_zstd1.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bs_zstd2 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_zstd2.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bs_zstd4 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_zstd4.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bs_zstd8 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_zstd8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    cpu_bs_zstd1 = cpu_bs_zstd1.drop(cpu_bs_zstd1.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_bs_zstd2 = cpu_bs_zstd2.drop(cpu_bs_zstd2.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_bs_zstd4 = cpu_bs_zstd4.drop(cpu_bs_zstd4.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_bs_zstd8 = cpu_bs_zstd8.drop(cpu_bs_zstd8.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)

    # remove last row (averages) 
    cpu_bs_zstd1.drop(cpu_bs_zstd1.tail(1).index, inplace=True)
    cpu_bs_zstd2.drop(cpu_bs_zstd2.tail(1).index, inplace=True)
    cpu_bs_zstd4.drop(cpu_bs_zstd4.tail(1).index, inplace=True)
    cpu_bs_zstd8.drop(cpu_bs_zstd8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    cpu_zstd = pd.concat([cpu_bs_zstd1, cpu_bs_zstd2, cpu_bs_zstd4, cpu_bs_zstd8], axis=1)
    cpu_zstd.index = np.arange(1, len(cpu_zstd) + 1)
    cpu_zstd.columns = ['1 process', '2 processes', '4 processes', '8 processes']

    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% CPU Used (System Mode): ZSTD-btrfs')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% CPU Used (System Mode)')
    plt.legend()
    cpu_zstd.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    cpu_zstd.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    cpu_zstd.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    cpu_zstd.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/cpu/zstd_bs_btrfs.png')
    plt.clf()
    del(cpu_zstd)
    print('Done printing zstd_bs_btrfs.png')


    # get data from txts for no compression
    cpu_bs_none1 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_none1.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bs_none2 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_none2.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bs_none4 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_none4.txt', skiprows=3, delim_whitespace=True, header=None)
    cpu_bs_none8 = pd.read_csv(root_dir + '/stress_tests/cpu/btrfs/cpu_none8.txt', skiprows=3, delim_whitespace=True, header=None)

    # remove unnecessary columns
    cpu_bs_none1 = cpu_bs_none1.drop(cpu_bs_none1.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_bs_none2 = cpu_bs_none2.drop(cpu_bs_none2.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_bs_none4 = cpu_bs_none4.drop(cpu_bs_none4.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)
    cpu_bs_none8 = cpu_bs_none8.drop(cpu_bs_none8.columns[[0, 1, 2, 3, 4, 6, 7, 8]], axis=1)

    # remove last row (averages) 
    cpu_bs_none1.drop(cpu_bs_none1.tail(1).index, inplace=True)
    cpu_bs_none2.drop(cpu_bs_none2.tail(1).index, inplace=True)
    cpu_bs_none4.drop(cpu_bs_none4.tail(1).index, inplace=True)
    cpu_bs_none8.drop(cpu_bs_none8.tail(1).index, inplace=True)
    
    # concat to one giant dataframe
    cpu_none = pd.concat([cpu_bs_none1, cpu_bs_none2, cpu_bs_none4, cpu_bs_none8], axis=1)
    cpu_none.index = np.arange(1, len(cpu_none) + 1)
    cpu_none.columns = ['1 process', '2 processes', '4 processes', '8 processes']

    # plot one line chart with all sessions in it. (4 lines total, one for each process test)
    ax = plt.gca()
    plt.title('% CPU Used (System Mode): No Compression-btrfs')
    plt.xlabel('Time (seconds)')
    plt.ylabel('% CPU Used (System Mode)')
    plt.legend()
    cpu_none.plot(kind='line', y='1 process', use_index=True, color='blue', ax=ax)
    cpu_none.plot(kind='line', y='2 processes', use_index=True, color='red', ax=ax)
    cpu_none.plot(kind='line', y='4 processes', use_index=True, color='black', ax=ax)
    cpu_none.plot(kind='line', y='8 processes', use_index=True, color='green', ax=ax)
    plt.savefig('plots/cpu/none_bs_btrfs.png')
    plt.clf()
    del(cpu_none)
    print('Done printing none_bs_btrfs.png')

if __name__ == '__main__':
    main()
