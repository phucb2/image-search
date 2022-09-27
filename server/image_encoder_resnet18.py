import torch.nn as nn
import torch
import torchvision.models as models

def get_encoding_model():
    resnet18 = models.resnet.resnet18(pretrained=True)
    resnet18_feature = nn.Sequential(*(list(resnet18.children())[:-1]))