import torch
import numpy as np
import torchvision.datasets as datasets

A = torch.eye(5)
print(A)
B = np.arange(0, 10)
print(B)
mnist_trainset = datasets.MNIST(root='./data', train=True, download=True, transform=None)
mnist_trainset.data[0:2].type(torch.float32)
pass