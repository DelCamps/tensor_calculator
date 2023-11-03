# PyTorch 3D Tensor Calculator

Welcome to my Machine Learning assignment where I've built a PyTorch module capable of performing various operations on 3D tensors. In this README, I will provide instructions for installation and usage of the module, as well as details about additional creative functions I've implemented.

## Introduction
For this assignment, I created a PyTorch module that can be used by the Machine Learning community. The module is designed to perform fundamental operations on 3D tensors using PyTorch.

## Installation
You can install my module using the following pip command:
```bash
pip install -U git+https://github.com/DelCamps/tensor_calculator.git

```
## Usage
Once you've installed the module, you can utilize it in your Python code as demonstrated below:

```python
import tensor_calculator.Tensor_Calculator as tc

# Create a tensor with all ones
ones_tensor = tc.TensorCalculator.tensor_ones(dim_x, dim_y, dim_z)

# Create a tensor with all zeros
zeros_tensor = tc.TensorCalculator.tensor_zeros(dim_x, dim_y, dim_z)

# Create a tensor with random values
random_tensor = tc.TensorCalculator.tensor_random(dim_x, dim_y, dim_z)

# Perform tensor addition
result_sum = tc.TensorCalculator.tensor_sum(tensor1, tensor2)

# Perform element-wise multiplication
result_multiply = tc.TensorCalculator.tensor_elementwise_multiplication(tensor, num)

# Perform matrix multiplication
result_matrix_multiply = tc.TensorCalculator.tensor_multiplication(tensor1, tensor2)

# Reshape a tensor
result_reshaped = tc.TensorCalculator.tensor_reshape(tensor, new_shape)

# Concatenate two tensors along a specified axis
result_concatenated = tc.TensorCalculator.tensor_concatenate(tensor1, tensor2, axis)

# Split a tensor along a specified axis
result_split = tc.TensorCalculator.tensor_split(tensor, split_size_or_sections, dim)
```
## Additional Functions

### tensor_elementwise_multiplication
#### Description
This function performs element-wise multiplication of a given tensor by a specified scalar value. It multiplies each element in the tensor by the provided scalar.

```python
result = tc.TensorCalculator.tensor_elementwise_multiplication(tensor, num)
```
### tensor_multiplication

#### Description
This function computes the matrix multiplication (dot product) between two input tensors. It is equivalent to performing matrix multiplication in 2D linear algebra.

```python
result = tc.TensorCalculator.tensor_multiplication(tensor1, tensor2)
```
### tensor_reshape
#### Description
This function reshapes a given tensor into a new shape specified by the user. The resulting tensor has the same total number of elements as the original tensor.


```python
result = tc.TensorCalculator.tensor_reshape(tensor, new_shape)
```
### tensor_concatenate
#### Description
This function concatenates two input tensors along a specified axis. It combines the tensors to create a larger tensor in the specified dimension.


```python
result = tc.TensorCalculator.tensor_concatenate(tensor1, tensor2, axis)
```
### tensor_split

#### Description
This function splits a given tensor along a specified axis into multiple smaller tensors. You can specify the size or the number of sections in which to split the tensor.


```python
result = tc.TensorCalculator.tensor_split(tensor, split_size_or_sections, dim)
```
