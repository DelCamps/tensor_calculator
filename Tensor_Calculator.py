import torch

__all__ = ['TensorCalculator']


class TensorCalculator():

    def __init__(self):
        return None

    def tensor_ones(dim_x, dim_y, dim_z):
        ones = torch.ones([dim_x, dim_y, dim_z])
        return ones

    def tensor_zeros(dim_x, dim_y, dim_z):
        zeros = torch.zeros([dim_x, dim_y, dim_z])
        return zeros


dim_x = 3
dim_y = 3
dim_z = 3

one_tensor = TensorCalculator.tensor_ones(dim_x, dim_y, dim_z)
print(one_tensor)