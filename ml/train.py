import os
import sys
import warnings
import logging
import time
from datetime import date
import pickle
from sklearn_porter import Porter
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
sys.path.append('../')
from utils.utils import create_dir

warnings.filterwarnings('ignore', category=UserWarning)
root_dir = str(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

def main():

    # create new directory for the current training session
    today = date.today()
    today = str(today.strftime('%m-%d-%Y'))
    dir_ = str(root_dir + '/saved_models/dtc-' + today)

    create_dir(dir_)

    # get training set
    data_path = str(root_dir + '/build/data.csv')
    df = pd.read_csv(data_path, header=None)
    
    # remove all time entries
    df = df.drop(columns=[3, 4])
    
    # clean filenames to only the extensions (file types)
    df.iloc[:, 0] = df.iloc[:, 0].apply(lambda x: x.split('.')[-1])
    encode = {'txt' : 0, 'jpg' : 1, 'h5' : 2, 'pdf' : 3, 'PDF' : 3}
    df.iloc[:, 0].replace(encode, inplace=True)

    # encode operation labels
    encode = {'compression' : 0, 'decompression' : 1}
    df.iloc[:, 3].replace(encode, inplace=True)

    # encode library labels
    encode = {'zstd' : 0, 'lzo' : 1, 'zlib' : 2}
    df.iloc[:, 4].replace(encode, inplace=True)

    # seperate data and labels
    x = df.iloc[:, : -1]
    y = df.iloc[:, -1:]

    # split training and testing data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0, shuffle=True)

    # train decision tree classifier
    dtree_model = DecisionTreeClassifier(max_depth = 2).fit(x_train, y_train)
    dtree_predictions = dtree_model.predict(x_test)

    # print resulting confusion matrix and classification report
    print(confusion_matrix(y_test, dtree_predictions))
    print(classification_report(y_test, dtree_predictions))

    # save python model
    pickle.dump(dtree_model, open(dir_ + '/dtc-python.sav', 'wb'))

    # transpile C version for model using porter
    porter = Porter(dtree_model, language='C')
    output = porter.export(embed_data=True)
    
    with open(root_dir + '/pred.cpp', 'w') as f:
        f.write(output)
if __name__ == '__main__':
    main()
