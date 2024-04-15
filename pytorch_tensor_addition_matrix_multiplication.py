import torch

# Addition
tensor_a = torch.tensor([1, 2, 3])
tensor_b = torch.tensor([4, 5, 6])
result = tensor_a + tensor_b
print(result)

# Matrix multiplication
matrix_a = torch.tensor([[1, 2], [3, 4]])
matrix_b = torch.tensor([[5, 6], [7, 8]])
result = torch.mm(matrix_a, matrix_b)
print(result)


