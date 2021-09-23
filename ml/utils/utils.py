import os
import random
import numpy as np
import torch

root_dir = str(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))


def create_dir(dir: str) -> None:
    if os.path.isdir(dir):
        print(dir, 'already exists. Continuing ...' )
    else:
         print('Creating new dir: ', dir)
         os.makedirs(dir)


# calculate accuracy of a prediction
def get_accuracy(prediction: str, label: str) -> float:
    matches  = [torch.argmax(i) == torch.argmax(j) for i, j in zip(prediction, label)]
    accuracy = matches.count(True) / len(matches)
    return accuracy
