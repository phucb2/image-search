from torchvision.datasets import ImageFolder
from torchvision import transforms
from torch.utils.data import (Dataset, DataLoader)
import os
import numpy as np
import random
from PIL import Image

tfms = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])

inv_tfms = transforms.Compose([
    transforms.Normalize(mean=1. / np.array([0.485, 0.456, 0.406]),
                         std=1. / np.array([0.229, 0.224, 0.225])),
    transforms.ToPILImage()
])


class ImageDataset(Dataset):
    def __init__(self, folder, tfms=None):
        self.folder = folder
        self.files = glob.glob(os.path.join(self.folder, '*.jpg'))

        self.tfms = tfms

    def __getitem__(self, index):
        img = Image.open(self.files[index])
        if self.tfms:
            img = self.tfms(img)
        return img, self.files[index]

    def __len__(self):
        return len(self.files)
