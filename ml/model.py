import torch
import torch.nn as nn
import torch.nn.functional as F

class lin_reg(nn.Module):
    def __init__(self):
        super(lin_reg, self).__init__()
        self.linear = nn.Linear(input_size, output_size)


    def forward(self, x):
        out = self.linear(x)
        return out
