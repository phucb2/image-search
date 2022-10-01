import ray
from ray.data.datasource import SimpleTorchDatasource
import torch
from torchvision import transforms
from torchvision.datasets.cifar import CIFAR10

transform = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
)


def train_dataset_factory():
    return CIFAR10(root='./data/', download=True, train=True, transform=transform)


def test_dataset_factory():
    return CIFAR10(root='./data/', download=True, train=False, transform=transform)


train_dataset: ray.data.Dataset = ray.data.read_datasource(SimpleTorchDatasource(),
                                                           dataset_factory=train_dataset_factory)

test_dataset: ray.data.Dataset = ray.data.read_datasource(SimpleTorchDatasource(),
                                                          dataset_factory=test_dataset_factory)
