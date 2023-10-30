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

    @staticmethod
    def tensor_reshape(tensor, new_shape):
        reshaped = torch.reshape(tensor, new_shape)
        return reshaped

    @staticmethod
    def tensor_concatenate(tensor1, tensor2, axis):
        concatenated_tensor = torch.cat((tensor1, tensor2), dim=axis)
        return concatenated_tensor

    @staticmethod
    def tensor_split(tensor, split_size_or_sections, dim):
        split_tensors = torch.split(tensor, split_size_or_sections, dim=dim)
        return split_tensors

