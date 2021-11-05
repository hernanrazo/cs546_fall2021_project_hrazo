import os
import sys
import warnings
import logging
import time
from datetime import date
import pickle
import pandas as pd
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
sys.path.append('../')
from utils.utils import create_dir

warnings.filterwarnings('ignore', category=UserWarning)
root_dir = str(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

def main():

    # create new directory for the current training session
    today = date.today()
    today = str(today.strftime('%m-%d-%Y'))
    dir_ = str(root_dir + '/saved_models/gbr-' + today)

    create_dir(dir_)

    # get training set
    data_path = str(root_dir + '/build/data.csv')
    df = pd.read_csv(data_path, header=None)

    # remove compression/decompression label
    df = df.drop(columns=3)

    # clean filenames to only the extensions (file types)
    df.iloc[:, 0] = df.iloc[:, 0].apply(lambda x: x.split('.')[-1])
    encode = {'txt' : 0, 'jpg' : 1, 'h5' : 2, 'pdf' : 3, 'PDF' : 3}
    df.iloc[:, 0].replace(encode, inplace=True)

    # encode library labels
    encode = {'zstd' : 0, 'lzo' : 1, 'zlib' : 2}
    df.iloc[:, 2].replace(encode, inplace=True)

    # encode operation labels
    encode = {'compression' : 0, 'decompression' : 1}
    df.iloc[:, 3].replace(encode, inplace=True)

    # seperate independent and dependent variables
    x = df.iloc[:, 0:3]
    y = df.iloc[:, 3:7]

    # split training and testing data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0, shuffle=True)
    
    grad_model = MultiOutputRegressor(GradientBoostingRegressor(learning_rate=0.1, n_estimators=200, max_depth=2)).fit(x_train, y_train)
    grad_pred = grad_model.predict(x_test)
    print('grad: ' + str(mean_squared_error(y_test, grad_pred)))

    # save python model
    pickle.dump(grad_model, open(dir_ + '/gbr-python.sav', 'wb'))
    
if __name__ == '__main__':
    main()
