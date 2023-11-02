# PyTorch 2D Tensor Calculator

Welcome to my Machine Learning assignment where I've built a PyTorch module capable of performing various operations on 2D tensors. In this README, I will provide instructions for installation and usage of the module, as well as details about additional creative functions I've implemented.

## Introduction
For this assignment, I created a PyTorch module that can be used by the Machine Learning community. The module is designed to perform fundamental operations on 2D tensors using PyTorch.

## Installation
You can install my module using the following pip command:

pip install https://github.com/DelCamps/tensor_calculator.git
Usage
Once you've installed the module, you can utilize it in your Python code as demonstrated below:

python
Copy code
import tensor_calculator.Tensor_Calculator as tc

# Create a tensor with all ones
ones_tensor = tc.tensor_ones(dim_x, dim_y, dim_z)

# Create a tensor with all zeros
zeros_tensor = tc.tensor_zeros(dim_x, dim_y, dim_z)

# Create a tensor with random values
random_tensor = tc.tensor_random(dim_x, dim_y, dim_z)

# Perform tensor addition
result_sum = tc.tensor_sum(tensor1, tensor2)

# Perform element-wise multiplication
result_multiply = tc.tensor_elementwise_multiplication(tensor, num)

# Perform matrix multiplication
result_matrix_multiply = tc.tensor_multiplication(tensor1, tensor2)

# Reshape a tensor
result_reshaped = tc.tensor_reshape(tensor, new_shape)

# Concatenate two tensors along a specified axis
result_concatenated = tc.tensor_concatenate(tensor1, tensor2, axis)

# Split a tensor along a specified axis
result_split = tc.tensor_split(tensor, split_size_or_sections, dim)
Additional Functions
As part of this assignment, I decided to go beyond the basic requirements and implemented additional functions to showcase my creativity and skills. These functions include:

Tensor Subtraction:

I added a function to subtract two tensors, allowing for more flexible tensor manipulation.
Matrix Transposition:

Another useful function I implemented is for transposing a 2D tensor, which can be handy for various data transformations.
Element-wise Division:

I created a function that performs element-wise division of two tensors, extending the range of operations available.
