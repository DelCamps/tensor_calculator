# PyTorch 2D Tensor Calculator

Welcome to my Machine Learning assignment where I've built a PyTorch module capable of performing various operations on 2D tensors. In this README, I will provide instructions for installation and usage of the module, as well as details about additional creative functions I've implemented.

## Introduction
For this assignment, I created a PyTorch module that can be used by the Machine Learning community. The module is designed to perform fundamental operations on 2D tensors using PyTorch.

## Installation
You can install my module using the following pip command:

```bash
pip install https://github.com/DelCamps/tensor_calculator.git
```

## Usage
Once you've installed the module, you can utilize it in your Python code as demonstrated below:

```python
import your_module_name as tm

# Create a tensor with all zeros
zeros_tensor = tm.zeros_tensor()

# Create a tensor with all ones
ones_tensor = tm.ones_tensor()

# Create a tensor with random values
random_tensor = tm.random_tensor()

# Perform tensor addition
result_sum = tm.add_tensors(tensor1, tensor2)

# Perform tensor multiplication
result_multiply = tm.multiply_tensors(tensor1, tensor2)
```

## Additional Functions
As part of this assignment, I decided to go beyond the basic requirements and implemented additional functions to showcase my creativity and skills. These functions include:

1. **Tensor Subtraction:**
   - I added a function to subtract two tensors, allowing for more flexible tensor manipulation.

2. **Matrix Transposition:**
   - Another useful function I implemented is for transposing a 2D tensor, which can be handy for various data transformations.

3. **Element-wise Division:**
   - I created a function that performs element-wise division of two tensors, extending the range of operations available.
