import torch

__all__ = ['TensorCalculator']


class TensorCalculator:

    def __init__(self):
        return None

    @staticmethod
    def tensor_ones(dim_x, dim_y, dim_z):
        ones = torch.ones([dim_x, dim_y, dim_z])
        return ones
    @staticmethod
    def tensor_zeros(dim_x, dim_y, dim_z):
        zeros = torch.zeros([dim_x, dim_y, dim_z])
        return zeros
    @staticmethod
    def tensor_random(dim_x, dim_y, dim_z):
        random = torch.rand([dim_x, dim_y, dim_z])
        return random
    @staticmethod
    def tensor_sum(tensor1, tensor2):
        sum_tensors = tensor1 + tensor2
        return sum_tensors
    @staticmethod
    def tensor_elementwise_multiplication(tensor,num):
        result = tensor * num
        return result
    @staticmethod
    def tensor_multiplication(tensor1, tensor2):
        result = torch.matmul(tensor1, tensor2)
        return result



dim_x = 3
dim_y = 3
dim_z = 3
num = 2

one_tensor = TensorCalculator.tensor_ones(dim_x, dim_y, dim_z)
print(one_tensor)

random_tensor = TensorCalculator.tensor_random(dim_x, dim_y, dim_z)
print(random_tensor)

sum_tensor = TensorCalculator.tensor_sum(one_tensor,random_tensor)
print(sum_tensor)

sum_tensor = TensorCalculator.tensor_sum(one_tensor,random_tensor)
print(sum_tensor)