# File name: model.py
import numpy as np
from transformers import pipeline
import torch.nn as nn
import torch
from PIL import Image
import torchvision.models as models
from torchvision import transforms


class Translator:
    def __init__(self):
        # Load model
        self.model = pipeline("translation_en_to_fr", model="t5-small")

    def translate(self, text: str) -> str:
        # Run inference
        model_output = self.model(text)

        # Post-process output to return only the translation text
        translation = model_output[0]["translation_text"]

        return translation


# translator = Translator()
#
# translation = translator.transla
# te("Hello world!")
# print(translation)


class Image2Vector:
    def __init__(self):
        pretrained = models.resnet.resnet18(pretrained=True)
        self.model = nn.Sequential(*(list(pretrained.children())[:-1]))

    def encode(self, file):
        tfms = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor()])

        img = Image.open(file)
        tensor = tfms(img)
        with torch.no_grad():
            print(tensor.shape)
            return self.model(tensor.unsqueeze(0)).squeeze().numpy()



if __name__ == '__main__':
    path = './../data/jpg/image_00001.jpg'
    pipeline = Image2Vector()
    file = open(path, 'rb')

    vector = pipeline.encode(file)
    print(vector.shape)
    print(vector.squeeze().shape)
    file.close()
